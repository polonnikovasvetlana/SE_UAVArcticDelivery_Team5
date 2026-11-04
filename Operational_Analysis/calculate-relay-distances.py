"""Reproduce first-pass WGS84 relay distances; does not assess flight feasibility."""

import csv
import ctypes as C
import ctypes.util
import heapq
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LIMIT_KM = 300.0


class Geodesic(C.Structure):
    _fields_ = [(name, C.c_double) for name in
                ('a', 'f', 'f1', 'e2', 'ep2', 'n', 'b', 'c2', 'etol2')] + [
        ('A3x', C.c_double * 6), ('C3x', C.c_double * 15),
        ('C4x', C.c_double * 21)]


library = C.util.find_library('proj')
if not library:
    raise SystemExit('Requires the PROJ shared library (geod_init/geod_inverse).')
lib = C.CDLL(library)
lib.geod_init.argtypes = [C.POINTER(Geodesic), C.c_double, C.c_double]
lib.geod_init.restype = None
lib.geod_inverse.argtypes = [C.POINTER(Geodesic)] + [C.c_double] * 4 + [
    C.POINTER(C.c_double)] * 3
lib.geod_inverse.restype = None
earth = Geodesic()
lib.geod_init(C.byref(earth), 6378137.0, 1 / 298.257223563)


def distance(a, b):
    result = C.c_double()
    lib.geod_inverse(C.byref(earth), *a, *b, C.byref(result), None, None)
    return result.value / 1000


# Check argument binding, ellipsoid scale, and date-line handling.
equatorial_degree = 2 * math.pi * 6378137 / 360 / 1000
assert abs(distance((0, 0), (0, 1)) - equatorial_degree) < 1e-8
assert abs(distance((0, 179), (0, -179)) - 2 * equatorial_degree) < 1e-8
assert distance((70, 120), (70, 120)) == 0

with (ROOT / 'relay-locations.csv').open(newline='') as file:
    sites = list(csv.DictReader(file))
by_id = {row['id']: row for row in sites}
assert len(by_id) == len(sites)
coordinates = {row['id']: (float(row['latitude']), float(row['longitude']))
               for row in sites}
assert all(-90 <= lat <= 90 and -180 <= lon <= 180
           for lat, lon in coordinates.values())
main = json.loads((ROOT / 'relay-chain-definition.json').read_text())['main_chain']
assert len(main) == len(set(main)) and all(key in by_id for key in main)

pairs = {}
for a, b in itertools.combinations(by_id, 2):
    value = distance(coordinates[a], coordinates[b])
    pairs[a, b] = pairs[b, a] = value


def path(start, end, allowed):
    queue = [(0.0, start, [start])]
    best = {start: 0.0}
    while queue:
        length, node, route = heapq.heappop(queue)
        if length > best[node]:
            continue
        if node == end:
            return route
        for other in allowed:
            if other == node:
                continue
            leg = pairs[node, other]
            new = length + leg
            if leg <= LIMIT_KM and new < best.get(other, float('inf')):
                best[other] = new
                heapq.heappush(queue, (new, other, route + [other]))
    return None


def leg(a, b):
    value = pairs[a, b]
    return {'from_id': a, 'from_name': by_id[a]['name'], 'to_id': b,
            'to_name': by_id[b]['name'], 'distance_km': f'{value:.6f}',
            'display_km': f'{value:.1f}', 'within_300_km': value <= LIMIT_KM,
            'near_threshold_295_305': 295 <= value <= 305,
            'interpretation': 'geographical_only_site_qualification_pending'}


def write_csv(name, rows):
    with (ROOT / name).open('w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


all_rows = [leg(a, b) for a, b in itertools.combinations(by_id, 2)]
write_csv('relay-pair-distances.csv', all_rows)
chain_rows = [dict(chain='illustrative_main', leg_number=i, **leg(a, b))
              for i, (a, b) in enumerate(zip(main, main[1:]), 1)]
residential = [key for key, row in by_id.items()
               if row['category'] == 'residential_candidate']
summary = {'method': 'PROJ geod_inverse; WGS84 ellipsoidal geodesic',
           'site_count': len(sites), 'pair_count': len(all_rows),
           'main_legs': len(chain_rows),
           'main_pass': sum(row['within_300_km'] for row in chain_rows),
           'main_gaps': [], 'paths': {}}
for row in list(chain_rows):
    if row['within_300_km']:
        continue
    alternative = path(row['from_id'], row['to_id'], list(by_id))
    summary['main_gaps'].append(dict(row, detour=alternative))
    if alternative:
        chain_rows.extend(dict(chain=f"detour_{row['from_id']}_{row['to_id']}",
                               leg_number=i, **leg(a, b))
                          for i, (a, b) in enumerate(zip(alternative, alternative[1:]), 1))
for label, allowed in [('all_candidates', list(by_id)),
                       ('residential_candidates_only', residential)]:
    route = path('MUR', 'ANA', allowed)
    summary['paths'][label] = route
    if route:
        chain_rows.extend(dict(chain=label, leg_number=i, **leg(a, b))
                          for i, (a, b) in enumerate(zip(route, route[1:]), 1))
alternative = ['CHR', 'BBI', 'PEV']
chain_rows.extend(dict(chain='alternative_CHR_PEV_via_Bilibino', leg_number=i,
                       **leg(a, b))
                  for i, (a, b) in enumerate(zip(alternative, alternative[1:]), 1))
write_csv('relay-chain-distances.csv', chain_rows)
(ROOT / 'relay-distance-results.json').write_text(
    json.dumps(summary, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(summary, indent=2, ensure_ascii=False))

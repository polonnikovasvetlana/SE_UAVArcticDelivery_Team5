"""One-way reach from existing candidate sites; representative NSR, not navigation advice."""
import argparse,csv,json,math,ctypes as C,ctypes.util
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--radius-km',type=int,default=300,help='One-way reach radius in kilometres (default: 300)')
args=parser.parse_args()
if args.radius_km<=0:
 parser.error('--radius-km must be positive')
radius_km=args.radius_km
suffix='' if radius_km==300 else f'_{radius_km}km'
# Reuse only the existing PROJ bindings, never execute its file-writing calculations.
exec((ROOT/'calculate-relay-distances.py').read_text().split('# Check argument binding')[0])
lib.geod_direct.argtypes=[C.POINTER(Geodesic)]+[C.c_double]*4+[C.POINTER(C.c_double)]*3
lib.geod_direct.restype=None

def direct(lat,lon,az,km):
 a,b=C.c_double(),C.c_double()
 lib.geod_direct(C.byref(earth),lat,lon,az,km*1000,C.byref(a),C.byref(b),None)
 return a.value,b.value

def inverse(a,b):
 d,z=C.c_double(),C.c_double()
 lib.geod_inverse(C.byref(earth),*a,*b,C.byref(d),C.byref(z),None)
 return d.value/1000,z.value

sites=list(csv.DictReader((ROOT/'relay-locations.csv').open()))
coords=[(float(s['latitude']),float(s['longitude'])) for s in sites]
source=json.loads((ROOT/'nsr-source-routes.json').read_text())
feature=next(f for f in source['features'] if f['attributes']['Name']=='Northern Sea Route')
a,b=feature['geometry']['paths']
# Restrict this historical line to Kara Sea entrance through Bering Strait.
route=[(lat,lon) for lon,lat in reversed(a) if lon>=58]
route += [(lat,lon) for lon,lat in list(reversed(b))[1:] if lat>=66.5]
samples=[]
for p,q in zip(route,route[1:]):
 km,az=inverse(p,q);n=math.ceil(km/5)
 for i in range(n):
  pt=direct(*p,az,km*(i+.5)/n)
  distances=[distance(pt,s) for s in coords];j=int(np.argmin(distances))
  samples.append(dict(lat=pt[0],lon=pt[1],weight_km=km/n,nearest_km=distances[j],site=sites[j]['name']))
total=sum(s['weight_km'] for s in samples)
covered=sum(s['weight_km'] for s in samples if s['nearest_km']<=radius_km)
avg=sum(s['nearest_km']*s['weight_km'] for s in samples)/total
worst=max(samples,key=lambda s:s['nearest_km'])
summary={'scope':'Historical representative line, Kara Sea entrance (~58E) to Bering Strait; not full shipping corridor',
 'coverage_radius_km':radius_km,
 'candidate_count':len(sites),'route_length_km':total,'covered_length_km':covered,'covered_percent':100*covered/total,
 'uncovered_length_km':total-covered,'length_weighted_mean_nearest_site_km':avg,'max_sampled_nearest_site_km':worst['nearest_km'],
 'worst_point':worst,'sampling_spacing_km_at_most':5,'upper_bound_for_continuous_line_required_radius_km':worst['nearest_km']+2.5,
 'assumptions':['All 57 candidates available (optimistic; electricity/permanent support not fully qualified).','One-way reach; recipient ship supports landing and compatible battery swap.','No wind, payload, energy reserve or recovery allowance.','No corridor width assumed; percentages measure route length, not sea area.']}
(ROOT/f'nsr-coverage-results{suffix}.json').write_text(json.dumps(summary,indent=2))
if radius_km==300:
 with (ROOT/'nsr-coverage-samples.csv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(samples[0]));w.writeheader();w.writerows(samples)
scale=math.cos(math.radians(70))
def display(lon):return lon%360
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig=plt.figure(figsize=(24,13),facecolor='#fbfcfd')
ax=fig.add_axes([.045,.31,.91,.56]);ax.set_facecolor('#eaf2f7')
land=json.loads((ROOT/'relay-map-land.geojson').read_text())
for f in land['features']:
 g=f['geometry'];polys=g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
 for poly in polys:
  ring=np.asarray(poly[0]);xs=np.degrees(np.unwrap(np.radians(ring[:,0])))
  for shift in (-360,0,360):
   x=xs+shift
   if x.max()>26 and x.min()<195 and ring[:,1].max()>61:
    ax.fill(x*scale,ring[:,1],fc='#e7e7dd',ec='#aabbb6',lw=.5,zorder=1)
for s,(lat,lon) in zip(sites,coords):
 pts=[direct(lat,lon,z,radius_km) for z in np.linspace(0,360,145)]
 xs=np.degrees(np.unwrap(np.radians([p[1] for p in pts])))
 xs+=360*round((display(lon)-xs[0])/360)
 ax.fill(xs*scale,[p[0] for p in pts],fc='#59af9d',ec='#298776',alpha=.14 if radius_km==300 else .08,lw=.65,zorder=2)
PORTS={'MUR','DIK','DUD','TIK','PEV','ANA'}
for s,(lat,lon) in zip(sites,coords):
 industrial=s['category']=='industrial_staff_candidate';port=s['id'] in PORTS
 ax.scatter(display(lon)*scale,lat,s=75 if port else 32,marker='D' if industrial else ('s' if port else 'o'),
  color='#c48720' if industrial else '#173f5d',edgecolors='white',linewidths=.6,zorder=5)
 if port or s['id'] in {'SAB','KHT','NIZ','CHO','RUS','POK','CHR'}:
  ax.annotate(s['name'],(display(lon)*scale,lat),xytext=(5,7 if s['id'] not in {'CHO','POK','CHR'} else -16),textcoords='offset points',
   fontsize=9,color='#173f5d',weight='bold' if port else 'normal',zorder=7,
   bbox=dict(fc='white',ec='none',alpha=.65,pad=.5))
# Color each sampled 5 km section by actual nearest-site WGS84 distance.
for p,q in zip(samples,samples[1:]):
 ax.plot([display(p['lon'])*scale,display(q['lon'])*scale],[p['lat'],q['lat']],
 color='#147854' if p['nearest_km']<=radius_km else '#cd3545',lw=4,zorder=4,solid_capstyle='round')
ax.scatter(display(worst['lon'])*scale,worst['lat'],marker='*',s=190,c='#a52738' if worst['nearest_km']>radius_km else '#173f5d',ec='white',zorder=8)
ax.annotate(f"Largest required reach: {worst['nearest_km']:.0f} km",(display(worst['lon'])*scale,worst['lat']),xytext=(0,26),
 textcoords='offset points',ha='center',color='#a52738' if worst['nearest_km']>radius_km else '#173f5d',weight='bold',bbox=dict(fc='white',ec='#cd3545' if worst['nearest_km']>radius_km else '#173f5d',pad=5),zorder=9)
ax.set_xlim(26*scale,195*scale);ax.set_ylim(61.5,82);ax.set_aspect('equal',adjustable='box')
ticks=np.arange(30,191,20);ax.set_xticks(ticks*scale,[f'{x}°E' if x<=180 else f'{360-x}°W' for x in ticks])
ax.set_yticks(np.arange(62,83,4),[f'{x}°N' for x in np.arange(62,83,4)])
ax.grid(alpha=.3,lw=.5);ax.tick_params(labelsize=9)
fig.text(.045,.955,f'NORTHERN SEA ROUTE  |  {radius_km} km ONE-WAY UAV COVERAGE',fontsize=24,weight='bold',color='#173f5d')
fig.text(.045,.922,'57 candidate launch sites • landing and battery swap on the receiving ship • WGS84 geodesic reach circles',fontsize=13,color='#536474')
handles=[Line2D([],[],color='#59af9d',lw=10,alpha=.5,label=f'{radius_km} km reach around each candidate'),
 Line2D([],[],color='#147854',lw=4,label=f'Reference route within {radius_km} km'),Line2D([],[],color='#cd3545',lw=4,label=f'Reference route beyond {radius_km} km'),
 Line2D([],[],ls='',marker='s',color='#173f5d',label='Reference port'),Line2D([],[],ls='',marker='o',color='#173f5d',label='Other relay candidate'),
 Line2D([],[],ls='',marker='D',color='#c48720',label='Conditional industrial site')]
fig.legend(handles=handles,loc='upper left',bbox_to_anchor=(.04,.305),ncol=3,frameon=False,fontsize=11)
fig.text(.045,.225,f"{radius_km} km reaches approximately {100*covered/total:.0f}% of this reference line ({covered:,.0f} / {total:,.0f} km).",fontsize=17,weight='bold',color='#173f5d')
fig.text(.045,.19,f"Average nearest-site distance: {avg:.0f} km. Complete reference-line coverage needs about {math.ceil((worst['nearest_km']+2.5)/10)*10:.0f} km nominal reach.",fontsize=15,color='#173f5d')
fig.text(.045,.148,'This is a historical representative route, not a defined corridor or current ice-dependent navigation track. No corridor width is assumed.',fontsize=11,color='#536474')
fig.text(.045,.122,'All 57 launch candidates are assumed available; electricity, permanent support, access and ship compatibility still require confirmation.',fontsize=11,color='#536474')
fig.text(.045,.096,'Circles include land and sea. Coverage is geographical only; wind, payload, reserves and the flight after the battery swap are not modeled.',fontsize=11,color='#536474')
fig.text(.045,.069,'Route source: Arctic Sea Routes feature service, credited to NGA; representative section ~58°E Kara Sea entrance to Bering Strait.',fontsize=10,color='#536474')
fig.text(.045,.046,f'Sources and calculation details: nsr-route-source.txt; nsr-coverage-results{suffix}.json; nsr-coverage-samples.csv. Coastline: Natural Earth, public domain.',fontsize=10,color='#536474')
fig.text(.045,.023,f'{"4" if radius_km==300 else "7"} November 2026 • Circles calculated on WGS84; display standard parallel 70°N. Route sampled every ≤5 km; radius bound includes 2.5 km sampling allowance.',fontsize=9,color='#536474')
for ext in (('png','pdf','svg') if radius_km==300 else ('png',)):
 fig.savefig(ROOT/f'Arctic_relay_map{suffix}.{ext}',dpi=170,facecolor=fig.get_facecolor())
print(json.dumps(summary,indent=2))

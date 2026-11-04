# Murmansk–Anadyr Relay Distances: First Pass

Calculated: 2026-11-04. Scope: a practical initial screen, with no map changes.

## Result

**Most legs in the selected illustrative chain are below 300 km, but there are four large direct gaps. Smaller settlements provide geometrical detour options around all four within the candidate list.** This does not establish that every coastal gap is below 300 km or that every candidate is an available, permanently staffed charging site.

- **57 candidate locations**, including small settlements and two conditional industrial locations.
- **1,596 unique pair distances calculated**: every pair in this 57-location list.
- Illustrative main chain: **37 locations / 36 legs; 32 legs (88.9%) at most 300 km; four exceed it**.
- Largest direct leg in that chain: **Dikson–Khatanga, 741.9 km**.
- Gyda–Dikson is **299.8 km** between the reference coordinates: too close to the threshold to assume that any chosen landing sites will pass.

The 88.9% figure describes this selected chain, not a statistically representative sample of all NSR settlements. The catalogue is a first pass, not an exhaustive inventory of every port, village, staffed station, or inland alternative.

## Direct Gaps and Candidate Detours

| Direct leg in illustrative chain | Direct distance | Calculated alternative, each leg at most 300 km | Evidence still needed |
| --- | --- | --- | --- |
| Dikson → Khatanga | **741.9 km** | Dikson → Vorontsovo (225.8) → Dudinka (273.4) → Norilsk (79.4) → Ust-Avam (262.9) → Kheta (249.2) → Khatanga (108.5). | Individual village electricity/access and permanent presence; this is a substantial inland detour. |
| Nizhneyansk → Chokurdakh | **435.7 km** | Nizhneyansk → Deputatsky (277.5) → Chkalov (226.4) → Chokurdakh (118.9). | Chkalov site supply and staffing; inland service implications. |
| Russkoye Ustye → Pokhodsk | **498.4 km** | Russkoye Ustye → Andryushkino (293.4) → Pokhodsk (259.5). | Current Andryushkino electricity/permanent presence; exact-site check on the 293.4 km leg. |
| Chersky → Pevek | **370.0 km** | Via Ayon: 293.8 + 92.3 km. Another option is **via Bilibino: 224.0 + 239.8 km**. | Ayon site qualification; Bilibino has operator supply evidence but creates an inland route. |

Distances in the alternatives are kilometres. The script chooses the shortest total detour from the listed candidate points; it does not optimize energy use, travel time, permitting, or ship coverage.

## What the End-to-End Network Check Found

Allowing every listed point, including the two conditional industrial candidates, yields a geographical Murmansk–Anadyr path with every step at most 300 km. It contains 26 legs, totals approximately **6,580 km**, and its longest leg is **298.1 km**. The exact ordered path is saved under `all_candidates` in the [distance-chain CSV](relay-chain-distances.csv) and [results JSON](relay-distance-results.json).

**This is an optimistic geographical path, not a verified operational network.** It relies on industrial candidates whose year-round staffing is not confirmed and on some residential candidates whose electricity evidence is only a regional lead. It also bypasses coastal destinations, so it cannot establish maritime-route coverage.

When both industrial candidates are removed, no all-legs-at-most-300-km Murmansk–Anadyr path was found in this particular catalogue. This does not prove that no residential-only route exists; additional settlements and inland detours could change the result.

## People and Electricity

These remain the two primary user criteria. They are stored separately for each location in [relay-locations.csv](relay-locations.csv):

- `people_evidence`: most points are registered settlements; registration is a useful location lead, not a fresh census or confirmation of permanent residents at the proposed relay address. Kharasavey and Sabetta are explicitly separated as industrial staffing candidates.
- `electricity_evidence`: distinguishes a named operator/supplier/plan record, historical evidence, a regional lead, and an unverified site. None establishes permission to connect a UAV charger or spare power capacity.
- `notes`: records coordinate proxies, access issues, and site-level questions.

Current operator material supports supply in several important places, including [Chersky, Bilibino and Pevek](https://chukotenergo.ru/o-kompanii/struktura-kompanii/), [Dudinka and Norilsk](https://oao-ntek.ru/company/about/profile/), [Khatanga](https://xn----8sbaaldjz6bg1a2a1b7g9a.xn--p1ai/), and [Deputatsky and Nizhneyansk](https://www.yakutskenergo.ru/press/news/news-company/71800/). Other sites have older evidence or require confirmation; the CSV does not label them as fully qualified relays.

## Method and Source Limits

Calculations use **WGS84 ellipsoidal geodesics** through the installed PROJ library: the shortest surface distance between reference coordinates. They include date-line crossing correctly. Values are rounded only for display; the 300 km test uses the unrounded calculation. They are not flown-route distances and contain no allowance for weather, energy reserves, or return/recovery.

Most coordinates are transcribed from the Russian State Catalogue of Geographical Names settlement registers published through Roskadastr. Source URLs are attached to each row. The registers identify settlements and coordinates, not electricity availability or current population. Full PDF downloads were unavailable through browsing; indexed extracts were used and the original links are retained for checking.

Registers used:

- [Murmansk region](https://kadastr.ru/upload/export_kadastr_files/%D0%9C%D1%83%D1%80%D0%BC%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C_202%D0%BD%D0%BF.pdf).
- [Nenets district](https://kadastr.ru/upload/export_kadastr_files/%D0%9D%D0%B5%D0%BD%D0%B5%D1%86%D0%BA%D0%B8%D0%B9%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3_202%D0%BD%D0%BF.pdf).
- [Krasnoyarsk / Taymyr](https://kadastr.ru/upload/export_kadastr_files/%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%8F%D1%80%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BA%D1%80%D0%B0%D0%B9_202%D0%BD%D0%BF.pdf).
- [Sakha (Yakutia)](https://kadastr.ru/upload/export_kadastr_files/%D0%A0%D0%B5%D1%81%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B0%20%D0%A1%D0%B0%D1%85%D0%B0%20%28%D0%AF%D0%BA%D1%83%D1%82%D0%B8%D1%8F%29_202%D0%BD%D0%BF.pdf).
- [Chukotka](https://kadastr.ru/upload/export_kadastr_files/%D0%A7%D1%83%D0%BA%D0%BE%D1%82%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3_202%D0%BD%D0%BF.pdf).

Additional coordinate sources are a registered Gyda entry in the general Yamal register, Getty's Seyakha record, an Arctic Council Kharasavey locality report, GeoNames' Sabetta airport record, and an official Norilsk environmental document. The last two are proxy points rather than selected relay installations; all five URLs are in the CSV. None of the coordinates was read from `Arc_map_full.png`.

Electrical evidence is linked separately in the CSV, including original operator publications and government plans/provider registers. Some government documents are available only as indexed extracts or mirrored original acts; those remain screening evidence, not a current on-site audit.

## Files and Reproduction

- [Location catalogue](relay-locations.csv) — Coordinates, settlement/staffing categories, electricity evidence, source URLs, and caveats.
- [Distance chain and detours](relay-chain-distances.csv) — All 36 main legs, detours, and the optimistic end-to-end path.
- [All candidate-pair distances](relay-pair-distances.csv) — All 1,596 pairs, with a 300 km flag.
- [Results JSON](relay-distance-results.json) — Counts, direct gaps, and path IDs.
- [Calculation script](calculate-relay-distances.py) and [chain definition](relay-chain-definition.json) — Run `python3 calculate-relay-distances.py` from this folder; requires the installed PROJ shared library. The script checks zero distance, equatorial scale, and date-line handling before calculating the files.

## PDR Wording

> A first-pass screen of 57 candidate locations found that 32 of 36 legs in an illustrative chain are within 300 km. Four direct gaps require intermediate relays or detours. A geographical end-to-end path is possible in the candidate set when inland and conditional industrial sites are allowed; electricity, permanent presence, access, and flight feasibility still require site-level confirmation.

This is the basis for further requirements discussion, not an approved change to workbook C2 or an assertion that all NSR relay gaps are below 300 km. See [ASM-001](../assumptions.md).

# Relay Network: Theory and Evidence Rules

Prepared: 2026-11-04. Stage: theoretical assessment and initial source screening.

**Current follow-up:** The user subsequently authorized a practical first-pass distance analysis. See [calculated results](relay-distance-first-pass.md), [location catalogue](relay-locations.csv), and [distance chain](relay-chain-distances.csv). The initial source-review limitations below describe the earlier theory stage; the follow-up has calculated distances but has not fully qualified sites. The no-map constraint still applies.

Project: **Emergency drug delivery to a ship or port based on UAV system with inflight data acquisition: temperature, pressure, winds and visibility measurements**

## User-Confirmed Scope

- Assess potential relay locations across the Murmansk–Anadyr operational corridor, including ports, small settlements, and existing facilities.
- The two primary screening parameters are **access to electricity** and **permanent human presence at the relay location**.
- Use straight-line distances for the first geographical assessment; the user also allows a file containing the chain of inter-station distances.
- Prepare theory first. Do not create or modify a map. `Arc_map_full.png` is a schematic reference, not a coordinate source.
- The proposition that consecutive relays can be connected by legs of at most 300 km is a hypothesis to test, not an approved aircraft capability or verified network property. See [ASM-001](../assumptions.md).

## 1. What Qualifies as a Candidate?

A location enters the screened network only when both conditions have supporting evidence:

**Candidate eligibility = electricity evidence AND permanent-presence evidence.**

| Parameter | Evidence to seek | What does not establish it |
| --- | --- | --- |
| Electricity | An operating local generator or supply network documented by the electricity operator, municipality, or a current infrastructure record. Grid connection is not necessary. | A planned power project, fuel storage alone, a heating/gas-service record, or an abandoned power station. |
| Permanent people | Evidence of a current residential community. A continuously staffed facility is a separate category pending confirmation that it meets the user's criterion. | Historical population, an abandoned village, occasional visitors, an automated station, or summer-only staffing. |

Record the two evidence statuses independently: **Documented**, **Uncertain**, or **Not met**, with source dates. A source documenting a settlement's power supply does not necessarily establish its current year-round population; neither parameter should be filled automatically from the other.

"Permanent presence" should initially mean residents living there year-round. Whether a facility with uninterrupted rotating staff is also acceptable remains an explicit interpretation question. Temporary expeditions and seasonal camps do not qualify on the current evidence rule.

Existing electricity supply is a screening condition. Permission to connect, usable power, and staff availability for UAV handling are later feasibility checks; they are not established by this first assessment. The same residents need not operate the relay unless that responsibility is separately agreed.

## 2. Location Categories

- **Port settlement:** inhabited location with port infrastructure and electricity evidence.
- **Other inhabited settlement:** permanent village/town with electricity; a port is not required.
- **Continuously staffed facility:** meteorological, research, industrial, or other facility; keep separate until year-round presence and eligibility are confirmed.
- **Uncertain or excluded lead:** retain its name and reason so future work does not repeatedly rediscover or accidentally admit it.

Port size is descriptive, not an eligibility criterion. Existing facilities with access constraints should retain that information; electricity and people do not imply permission to use the site.

## 3. How to Test the 300 km Hypothesis

1. Build an evidence-backed candidate register and obtain sourced coordinates. Use the same datum, preferably WGS84, which specifies a standard Earth reference for coordinates.
2. Calculate shortest surface distances between coordinate pairs using an ellipsoidal geodesic calculation. This is the geographical interpretation of the user's straight-line screening rule, not a measurement from the schematic map.
3. Treat eligible locations as network nodes. Connect a pair when their distance is at most 300 km. Evaluate the unrounded distance; display rounded kilometres separately.
4. Check for a connected path from Murmansk to Anadyr. Test all relevant pairs, not just an arbitrary eastward ordering or each site's nearest neighbour.
5. For a proposed chain, list every leg, distance, source-coordinate references, and evidence status. Report the longest leg and all legs exceeding 300 km.
6. Search for intermediate inhabited/powered locations around a gap. A gap between two major ports alone does not disprove the possibility of a chain through smaller settlements.

If the screened network is disconnected, the supported conclusion is **"no complete path found in the documented candidate set"**, not "no such sites exist anywhere." Network feasibility depends on catalogue completeness. Approximate coordinates near the threshold require more precise site coordinates before a definitive pass/fail decision.

If a gap of length D were filled by new perfectly placed relays, at least `ceil(D / 300) − 1` intermediate points would be needed. This is only a geometric lower bound: it does not establish the existence of electricity or permanent people at those positions.

## 4. Keep Four Questions Separate

| Question | Meaning |
| --- | --- |
| Relay connectivity | Can the documented stations connect Murmansk to Anadyr using legs of at most 300 km? |
| Ship/port service coverage | Which intended recipients are reachable from stations? A connected coastal chain does not establish coverage of offshore shipping routes. |
| Aircraft mission feasibility | Can the selected UAV fly a particular loaded leg in the specified weather with the required reserves and recovery arrangement? |
| Service response time | Can medicine reach the recipient within the agreed end-to-end time, including preparation and intermediate stops? |

The user's approved geographical measurement method settles none of the other three questions. Existing workbook C2 (300 km to a ship) is a different quantity from a 300 km relay-to-relay leg. Preserve that distinction.

Also distinguish charging at a station from swapping a battery. A swap can reduce the aircraft's stop time, but the station still needs sufficient charging throughput for subsequent missions. No battery size, charger power, charging time, or spare-battery stock has yet been selected.

## 5. Initial Web Evidence and Its Limits

Sources were checked on 2026-11-04. This is an initial source review, not a completed location inventory. No coordinates or inter-station distances have been verified in this stage.

| Area / example | Evidence found | What remains to establish |
| --- | --- | --- |
| Kola coast: Teriberka / Ostrovnoy | Rosseti operator publications describe residential supply in Teriberka and a supply line to Ostrovnoy. [S1], [S2] | Publications are historical; confirm current supply and year-round presence at each proposed location. |
| Nenets coast | An official regional infrastructure-plan PDF was found, but full retrieval failed. It is a research lead only. [S3] | Read the current regional plan and identify electricity operators for individual settlements; establish permanent population separately. |
| Khatanga | The local electricity operator describes operating diesel generation, residential service, and employees; its website has 2026 notices. [S4] | Establish the exact relay site and access to supply; record a current residential-presence source. This evidence does not automatically apply to other Taymyr villages. |
| Yakutia / Tiksi | RusHydro's January 2026 operator publication describes electricity service to remote settlements and a wind-diesel complex at Tiksi. [S5] | Verify each smaller settlement independently, including current permanent presence. A regional operator description is not a station-by-station inventory. |
| Eastern corridor: Chersky, Pevek, Egvekinot, Amguema, Anadyr | Chukotenergo identifies settlements supplied by its electricity networks. [S6] | Confirm current permanent communities and individual sites. The undated page contains legacy technical information; do not reuse its plant capacities as current facts. |

### Sources

- **S1 — Rosseti, 2020 residential electricity-service report, Teriberka:** [operator publication](https://www.mrsksevzap.ru/press/news/newsfilials/news81534.html). Search-index text was available; full-page retrieval failed. Treat as historical screening evidence, not confirmation of 2026 operation.
- **S2 — Rosseti, supply-network report including Ostrovnoy:** [operator publication](https://www.mrsksevzap.ru/press/news/newsrossetisz/news85544.html). Search-index text was available; full-page retrieval failed. Historical lead requiring current confirmation.
- **S3 — Nenets regional infrastructure plan, 2017:** [regional government PDF](https://gkh.adm-nao.ru/media/uploads/userfiles/2017/11/23/%D0%9F%D0%97_%D0%A1%D0%A2%D0%9F_%D0%9D%D0%90%D0%9E_%D0%A2%D0%BE%D0%BC_1.pdf). Located in search; retrieval timed out. Not accepted as verified site-level evidence.
- **S4 — Khatanga electricity operator, Energia:** [official operator website](https://xn----8sbaaldjz6bg1a2a1b7g9a.xn--p1ai/), introductory description of electricity generation/distribution and residential service; 2026 notices visible. Page read.
- **S5 — RusHydro, January 2026, Sakhaenergo:** [operator publication](https://www.vestnik-rushydro.ru/articles/1-yanvar-2026/data/po-doroge-smelykh-resheniy/), section on remote-settlement supply and Tiksi. Page read.
- **S6 — Chukotenergo, company structure / supply geography:** [official operator website](https://chukotenergo.ru/o-kompanii/struktura-kompanii/), description of settlements supplied in the Chaun–Bilibino, Egvekinot, and Anadyr networks. Page read; publication date not established.

Operator sources establish leads about infrastructure; final eligibility still requires the two separate evidence checks. No station is declared fully qualified solely by this initial table.

## 6. Planned Data Outputs After the Theoretical Stage

The user has allowed a distance-chain file. Populate it with calculated results only after coordinates and candidate evidence have been collected; do not invent values or imply the chain is already proven.

- `relay-locations.csv`: stable ID, names/aliases, region, category, latitude, longitude, coordinate source/precision, people evidence/status/date, electricity evidence/status/date, local operator, seasonality, eligibility, access notes, and unresolved questions.
- `relay-chain-distances.csv`: chain/leg ID, origin ID, destination ID, unrounded and displayed distance, 300 km screening result, coordinate references, node eligibility status, and notes about gaps or missing evidence.

These initially proposed files have now been populated in the first-pass follow-up linked above, with site-level evidence limitations recorded. No maps have been created or modified. Source evidence is linked per location, not just placed in a general bibliography.

## 7. Questions Before a Defensible Chain Can Be Claimed

- Do continuously staffed facilities with rotating crews qualify, or only permanent residential communities?
- How far inland may a relay route detour? A mainland settlement chain and coverage along the maritime route are different operational concepts.
- Is year-round service required, or can a seasonal power limitation be compatible with the mission? The present screening rule requires permanent people and flags seasonal electricity separately.
- Is 300 km a hard geographical screening threshold or a proposed aircraft loaded-leg requirement? It is presently used only for screening.

Next work is a source-backed station inventory and coordinate assessment under these rules. Record resulting numerical requirements in System Analysis only after review. See [project status](../status.md), [decisions](../decision-log.md), and [assumptions](../assumptions.md).

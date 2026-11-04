# Project Status

Last updated: 2026-11-04.

## Current Milestone

- Main objective: Prepare for the PDR defense against the nine deliverables in the user-provided image. See [PDR preparation notes](PDR/README.md) for the checklist, current evidence, proposed sequence, and open questions.
- The user reports that Operational Analysis has been performed.
- The existing reports and Capella model also contain developed System Analysis. Formal approval of an engineering baseline has not been recorded here.
- Logical and physical architecture contain mostly initial placeholders.
- Next review: PDR. Defense date, submission deadline, and required presentation/report format are not yet confirmed.
- Exact project title and scope: Confirmed by the user and preserved in [README.md](README.md) and [project instructions](../AGENTS.md).

## Completed Work

- Created an IDEF0 functional decomposition, described in the [Part 1 report](../SE_my_notes/Problem%20set%202/Team5_problem2_part1.docx).
- Developed stakeholder groupings, operational capabilities and activities, system functions, and delivery scenarios in the [Part 2 report](../SE_my_notes/Problem%20set%202/Team5_problem2_part2.docx) and [Capella model](Capella/UAV_Delivery_Arctic.capella).
- Inspected these materials and the requirements questions workbook for project context on 2026-11-04. This was a contextual review, not a full model validation.
- Restored project coordination files after the user reported a Git repository issue.
- Created separate Operational Analysis and System Analysis summaries for future agent context, linked below.
- Recorded the user's PDR deliverables and preparation notes, distinguishing course requirements from proposed work and unassessed readiness.

## Engineering Context for Future Work

- [Operational Analysis current state](Operational_Analysis/README.md) — Stakeholders, operational capabilities and flows, existing diagrams, and handoff to SA.
- [System Analysis current state](System_Analysis/README.md) — System boundary and allocations, delivery cases, scenarios, traceability, and provisional quantitative inputs.
- Both summaries preserve ship or port delivery and inflight temperature, pressure, winds and visibility measurements as project scope. They describe existing evidence without establishing engineering approval.

## Active Tasks

- Updated the existing [relay map](Operational_Analysis/Arctic_relay_map.png) to show 300 km one-way coverage, with PDF/SVG exports. A sourced historical NSR reference line gives 46.8% length coverage, 312 km mean nearest-site distance and approximately 630 km reach for that line alone; this does not define the full shipping corridor. See [coverage summary](Operational_Analysis/nsr-coverage-summary.md). User specifies landing and battery swap on the receiving ship; site and ship support remain unverified.

- Created a separate [relay map](Operational_Analysis/Arctic_relay_map.png) on 2026-11-04 at the user's request, with PDF/SVG exports, 57 candidates, reference-port/relay/industrial symbols, four highlighted direct gaps over 300 km, and candidate detours. Original maps are unchanged. Port grouping follows the reference map, not verified throughput; sites and detours remain provisional.

- PDR preparation remains the project priority. Current work concerns service coverage and relay connectivity from Murmansk to Anadyr.
- [First-pass distance analysis](Operational_Analysis/relay-distance-first-pass.md) is complete: 57 candidate locations, all 1,596 unique pair distances, a 36-leg illustrative chain, direct gaps, and candidate detours. The user requested a practical first pass rather than exhaustive research. No maps were changed.
- In the illustrative chain, 32 of 36 legs are at most 300 km. Four direct gaps exceed it; geographical detours exist in the candidate set. An optimistic end-to-end path exists when conditional industrial sites and inland routing are allowed, but a fully qualified electricity/permanent-presence network is not proven (ASM-001).
- [Relay-network theory](Operational_Analysis/relay-network-theory.md) retains the two primary site criteria: electricity and permanent human presence. The [location CSV](Operational_Analysis/relay-locations.csv) records coordinates and separates operator/plan/historical evidence from regional leads and unverified electricity. Source retrieval limits and coordinate proxies are documented.

## Blockers and Open Questions

- For relay screening, confirm whether continuously staffed facilities with rotating crews qualify as permanent human presence, and define acceptable inland detours. These choices affect which locations may connect the corridor.
- Review the four direct gaps and proposed detours in the distance report. Gyda–Dikson is 299.8 km between reference coordinates, so exact landing-site selection can change the 300 km screening result.
- Reconcile delivery-time targets: Part 1 states no more than 3 hours for shore sites and 5 hours for ships; Part 2 and workbook entry A4 give 4 hours.
- Validate quantitative inputs before treating them as approved requirements. The [workbook](Operational_Analysis/UAV_NFR_Questions.xlsx) contained 55 questions: 54 marked Open, one Assumed, and none Confirmed during the earlier review. It is now located in `Operational_Analysis/`.
- Confirm maximum target-ship speed (C3), which is blank. Transit time (C4) is a formula with no cached result in the inspected workbook.
- The two workbook copies were identical during the earlier review. The currently located copy is `Operational_Analysis/UAV_NFR_Questions.xlsx`; confirm it as authoritative before editing its engineering content.
- Confirm the PDR defense date, submission format, team responsibilities, and approval status of existing artifacts.
- Assess all nine PDR deliverables; several management and evidence-planning documents have not yet been reviewed. Logical architecture is explicitly required by the checklist and remains mostly initial placeholders.

## Proposed Next Steps

1. Review the completed first-pass relay results with the user; select a candidate route and confirm electricity/permanent presence at its critical nodes. Preserve the no-map constraint and distinguish inland connectivity from ship-route coverage.
2. Consolidate the operating concept and reconcile conflicting targets, distinguishing verified facts from assumptions and proposed requirements.
3. Use the existing operational and system functions as inputs to the logical architecture required for PDR. A completed physical architecture is not explicitly required by the supplied checklist.
4. Within authorized work, record resulting decisions and assumptions in [decision-log.md](decision-log.md) and [assumptions.md](assumptions.md).

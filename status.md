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

- PDR preparation is the current project priority. Initial notes and deliverable mapping are complete; the next engineering work package has not yet been agreed.

## Blockers and Open Questions

- Reconcile delivery-time targets: Part 1 states no more than 3 hours for shore sites and 5 hours for ships; Part 2 and workbook entry A4 give 4 hours.
- Validate quantitative inputs before treating them as approved requirements. The [workbook](UAV_NFR_Questions.xlsx) contains 55 questions: 54 marked Open, one Assumed, and none Confirmed during the review.
- Confirm maximum target-ship speed (C3), which is blank. Transit time (C4) is a formula with no cached result in the inspected workbook.
- Select the authoritative workbook: `UAV_NFR_Questions.xlsx` and `Research/UAV_NFR_Questions.xlsx` were identical during the review.
- Confirm the PDR defense date, submission format, team responsibilities, and approval status of existing artifacts.
- Assess all nine PDR deliverables; several management and evidence-planning documents have not yet been reviewed. Logical architecture is explicitly required by the checklist and remains mostly initial placeholders.

## Proposed Next Steps

1. Use the [PDR checklist](PDR/README.md) to agree the next work package and expected output with the user.
2. Consolidate the operating concept and reconcile conflicting targets, distinguishing verified facts from assumptions and proposed requirements.
3. Use the existing operational and system functions as inputs to the logical architecture required for PDR. A completed physical architecture is not explicitly required by the supplied checklist.
4. Within authorized work, record resulting decisions and assumptions in [decision-log.md](decision-log.md) and [assumptions.md](assumptions.md).

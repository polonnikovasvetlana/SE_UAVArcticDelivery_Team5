# PDR Preparation Notes

Last updated: 2026-11-04.

## Current Goal and Source

The user's current main goal is to prepare for the **Preliminary Design Review (PDR) defense**.

Project: **Emergency drug delivery to a ship or port based on UAV system with inflight data acquisition: temperature, pressure, winds and visibility measurements**

The deliverable requirements below are transcribed from the user-provided image headed “PDR deliverables” in this conversation on 2026-11-04. The image has not been saved as a repository file. It lists nine required deliverables, not an explicit execution order. Preparation suggestions in this document are working notes, not additional instructor requirements or approved design decisions.

## Required Deliverables and Current Evidence

The identifiers below are local checklist labels, not identifiers supplied by the instructor. “Not assessed” means readiness has not been established; it does not prove that team material does not exist elsewhere.

| ID | Required deliverable from the image | Current evidence / readiness | Proposed next work |
| --- | --- | --- | --- |
| PDR-01 | MBSE model of the system based on Arcadia-Capella – including stakeholders’ analysis, operational analysis, systems analysis and logical architecture | Stakeholders, OA, and SA are developed in the existing model and reports. Logical architecture is mostly initial placeholders. Full consistency and approval are not established. | Review existing layers; develop logical architecture and trace links from needs through functions to logical components. |
| PDR-02 | ConOps of the proposed system | Delivery scenarios exist in reports/model. The current `ConOps/README.md` is empty; a dedicated ConOps has not been reviewed. | Consolidate the operating concept for ship and port delivery, inflight measurements, roles, normal operation, and abnormal situations. |
| PDR-03 | Clear set of technical requirements | The workbook has 55 questions: 54 Open, one Assumed, none Confirmed in the current review. Delivery-time targets conflict. | Reconcile targets; produce uniquely identified, measurable requirements with sources, assumptions, and verification methods. |
| PDR-04 | Project management plan including WBS | Not assessed; no reviewed dedicated plan identified in the inspected material. | Define deliverables, responsibilities, dependencies, schedule, and a Work Breakdown Structure (WBS): a breakdown of the project into manageable work packages. |
| PDR-05 | Risk analysis | Not assessed; no reviewed risk register identified. | Identify and assess risks, their causes and consequences, mitigation actions, and owners. |
| PDR-06 | System verification and validation plans | Not assessed; no reviewed dedicated plans identified. | Plan verification against technical requirements and validation against stakeholder needs and operational scenarios. |
| PDR-07 | Interface management plan | Actors and exchanges provide starting inputs in SA; no reviewed dedicated management plan identified. | Identify interfaces and responsible parties; define what is exchanged, constraints, documentation, and change coordination. |
| PDR-08 | Configuration management and data management baseline plan | Git is used, and a repository issue caused lost files. This does not constitute a reviewed management plan. | Define controlled artifacts, identifiers/versions, review and change rules, baseline contents, authoritative copies, storage, backup, and recovery. |
| PDR-09 | Compliance check with maritime regulations | Authorities are modeled, but no reviewed compliance assessment is identified. | Confirm operational jurisdiction and applicable maritime rules, then map obligations to design evidence and open actions using current official sources. |

MBSE means **model-based systems engineering**: using linked system models as engineering evidence. ConOps means **Concept of Operations**: how the proposed service is intended to operate in its real context. See [Operational Analysis](../Operational_Analysis/README.md) and [System Analysis](../System_Analysis/README.md) for the existing model descriptions and source links.

## Important Preparation Notes

- Preserve both service outputs throughout the defense: medicine delivery to a ship or port, and inflight temperature, pressure, winds and visibility measurements. Weather acquisition is not an optional addition.
- Logical architecture is explicitly required by the image. A completed physical architecture is not explicitly listed; confirm expectations before expanding the preparation scope.
- Existing diagrams and populated spreadsheet cells do not establish deliverable readiness. Track evidence, consistency, and unresolved assumptions before proposing an artifact as ready for review.
- Reconcile the 3-hour shore / 5-hour ship delivery statements with the 4-hour statement. Keep this unresolved until the user agrees the target and supporting basis.
- Current range study uses 312 km average nearest-candidate distance and approximately 630 km one-way reach for full coverage of the selected reference route. Main shipping areas take priority and full coverage is optional; the acceptance target remains undefined. Present these as geographical benchmarks, with their limits, rather than approved aircraft requirements. See the [technical requirements / agent brief](../System_Architecture/technical-requirements-brief.md) and DEC-003.
- Keep package-temperature preservation separate from ambient-temperature measurement requirements; they concern different functions.
- Verification asks whether the system satisfies its specified requirements. Validation asks whether it serves the intended stakeholder needs and operating context. Both plans are required.
- Keep the maritime compliance check explicit. Any aviation or other regulatory assessment identified later should complement it rather than replace it. This document makes no finding of legal applicability or compliance.
- Do not invent a PDR date, presentation duration, slide count, team assignments, or numerical acceptance criteria; none is supplied by the image.

## Proposed Preparation Sequence

1. Confirm the defense date, submission format, and division of work; assess all nine deliverables against existing team material.
2. Develop ConOps and resolve the key technical requirements together, using existing OA/SA rather than starting again.
3. Develop and review logical architecture in Capella, preserving traceability to requirements and system functions. Feed risk and compliance findings into design choices as they emerge.
4. Develop the management, risk, verification/validation, interface, configuration/data, and maritime-compliance deliverables alongside the design work.
5. Cross-check the complete package and prepare the defense narrative: needs → operating concept → requirements → logical solution → risks, evidence plans, and controlled baseline.

This sequence is a proposal, not authorization to execute every task. The current request authorizes recording notes and project context; subsequent engineering changes must follow the user's explicit authorization rules.

## Open Questions

- When is the defense, and when must artifacts be submitted?
- What presentation/report format and assessment rubric apply beyond the image?
- Which deliverables already exist in team files outside this directory?
- Who owns each deliverable, and how are team approvals recorded?
- Which operating area and jurisdiction should frame the compliance assessment?

Maintain overall progress in [status.md](../status.md). Record engineering decisions and assumptions in [decision-log.md](../decision-log.md) and [assumptions.md](../assumptions.md), without treating this checklist as an approved engineering baseline.

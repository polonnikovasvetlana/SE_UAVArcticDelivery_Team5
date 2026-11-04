# Emergency drug delivery to a ship or port based on UAV system with inflight data acquisition: temperature, pressure, winds and visibility measurements

**Systems Engineering Project | Skoltech 2026 | Team 5**

This repository contains the documentation, analysis, and system models developed for the Systems Engineering course.

## Project Coordination

- [PDR preparation notes](PDR/README.md) — Current main goal, nine required deliverables, existing evidence, gaps, and proposed preparation sequence.
- [Current status](status.md) — Progress, current work, open questions, and next steps.
- [Decision log](decision-log.md) — Proposed, approved, and superseded engineering decisions, with reasons and evidence.
- [Assumptions](assumptions.md) — Unconfirmed assumptions, their consequences, and how to verify them.

## Repository Structure

- [Operational_Analysis/](Operational_Analysis/README.md) — Current stakeholder model, capabilities, operational flows, evidence, and open questions; start here for OA tasks.
- [System_Analysis/](System_Analysis/README.md) — Current system boundary, functions, scenarios, traceability, provisional inputs, and next steps; start here for SA tasks.
- **Stakeholder_Analysis/** — Stakeholder identification, needs, expectations, and requirements.
- **ConOps/** — Concept of Operations, operational scenarios, and system use cases.
- [System_Architecture/](System_Architecture/README.md) — Architecture study and current [technical requirements / agent brief](System_Architecture/technical-requirements-brief.md).
- **Capella/** — Arcadia models and Capella project files.

## Existing Engineering Inputs

- [IDEF0 report](../SE_my_notes/Problem%20set%202/Team5_problem2_part1.docx) — Functional decomposition of delivery and inflight weather-data acquisition.
- [Operational and System Analysis report](../SE_my_notes/Problem%20set%202/Team5_problem2_part2.docx) — Stakeholders, capabilities, activities, system functions, and delivery scenarios.
- [Capella model](Capella/UAV_Delivery_Arctic.capella) — Existing Operational Analysis and System Analysis; open with the associated `.aird` and `.afm` files in this folder.
- [Requirements questions workbook](Operational_Analysis/UAV_NFR_Questions.xlsx) — Preliminary quantitative inputs. Earlier copies were identical during the 2026-11-04 review; the currently located copy is in `Operational_Analysis/`. Confirm it as authoritative before editing its engineering content.

These inputs have been inspected for context; inspection does not establish formal approval or technical validation. Identify authoritative requirements and architecture artifacts here as they are agreed.

## Project Overview

The project covers emergency drug delivery to a ship or port using a UAV system, with inflight acquisition of temperature, pressure, winds and visibility measurements.

The existing analysis considers the Northern Sea Route and remote Arctic environments. The system aims to enable fast, reliable, and safe delivery of medical supplies while acquiring the inflight measurements described above.

Current UAV range comparison uses two geographical benchmarks: **312 km average distance to the nearest candidate launch site**, and **approximately 630 km one-way reach for full coverage of the selected reference shipping-route line**. The user prioritizes the main shipping areas; complete coverage is not mandatory. The average is not a proven minimum aircraft range or a guarantee of majority coverage. See the [current agent brief](System_Architecture/technical-requirements-brief.md) and [coverage evidence](Operational_Analysis/nsr-coverage-summary.md).

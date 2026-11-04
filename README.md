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
- **System_Architecture/** — System architecture, functional decomposition, interfaces, and design decisions.
- **Capella/** — Arcadia models and Capella project files.

## Existing Engineering Inputs

- [IDEF0 report](../SE_my_notes/Problem%20set%202/Team5_problem2_part1.docx) — Functional decomposition of delivery and inflight weather-data acquisition.
- [Operational and System Analysis report](../SE_my_notes/Problem%20set%202/Team5_problem2_part2.docx) — Stakeholders, capabilities, activities, system functions, and delivery scenarios.
- [Capella model](Capella/UAV_Delivery_Arctic.capella) — Existing Operational Analysis and System Analysis; open with the associated `.aird` and `.afm` files in this folder.
- [Requirements questions workbook](UAV_NFR_Questions.xlsx) — Preliminary quantitative inputs. A second copy exists in `Research/`; the copies were identical during the 2026-11-04 review. The authoritative copy remains to be agreed.

These inputs have been inspected for context; inspection does not establish formal approval or technical validation. Identify authoritative requirements and architecture artifacts here as they are agreed.

## Project Overview

The project covers emergency drug delivery to a ship or port using a UAV system, with inflight acquisition of temperature, pressure, winds and visibility measurements.

The existing analysis considers the Northern Sea Route and remote Arctic environments. The system aims to enable fast, reliable, and safe delivery of medical supplies while acquiring the inflight measurements described above.

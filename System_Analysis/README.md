# System Analysis — Current State

Last reviewed: 2026-11-04.

Project: **Emergency drug delivery to a ship or port based on UAV system with inflight data acquisition: temperature, pressure, winds and visibility measurements**

## Status and Purpose

System Analysis (SA) is developed in the existing report and Capella model. It defines the system boundary, external actors, system functions, and delivery scenarios. Formal approval of a requirements baseline and full model validation are not recorded. Logical and physical architecture contain mostly initial placeholders.

SA treats the automated system as a black box: it describes responsibilities and external interactions before choosing the internal components. Start with the [Operational Analysis summary](../Operational_Analysis/README.md) when stakeholder context is needed.

## Source Files

- [Part 2 report, sections 2–3](../../SE_my_notes/Problem%20set%202/Team5_problem2_part2.docx) — System boundary, capabilities, delivery cases, exchange scenario, and quantitative inputs.
- [Capella model, System Analysis layer](../Capella/UAV_Delivery_Arctic.capella) and [diagram file](../Capella/UAV_Delivery_Arctic.aird) — Model elements, allocations, traceability, and representations.
- [Part 1 IDEF0 report](../../SE_my_notes/Problem%20set%202/Team5_problem2_part1.docx) — Complementary functional decomposition and earlier performance statements.
- [Requirements questions workbook](../Operational_Analysis/UAV_NFR_Questions.xlsx) — Provisional quantitative inputs. Earlier copies were identical during review; the currently located copy is in `Operational_Analysis/`. Confirm it as authoritative before engineering edits.

Consult these sources before changing model content. This document summarizes them; it does not approve their numerical values.

## System Boundary and Responsibilities

**The current System is the automated delivery equipment and software, while Mission control is the human operator or team supervising it.**

The Capella component named `System` has 12 function allocations, covering transport, weather collection, route generation and updates, flight execution/replanning, package-temperature preservation, handover, status reporting, package acceptance, and connection with the ship.

| Responsibility | Existing functions allocated to System |
| --- | --- |
| Delivery | `Transport package to the site`, `Take the medicine`, `Hand over package` |
| Route and flight | `Build initial route`, `Take updates from the mission control`, `Execute trajectory: better weather, avoid obstacles`, `Replan the trajectory` |
| Medicine protection | `Keep package temperature` |
| Inflight data acquisition | `Collect weather data on the way`, `Monitor and report the weather` — temperature, pressure, winds and visibility measurements |
| External communication | `Report flight status`, `Establish connection with a ship` |

Human **Mission control** remains an external actor: it accepts requests, requests approvals, launches and tracks delivery, and issues change or abort orders. The medical chain decides treatment and supplies medicine. Receiving-site personnel receive the package. Authorities, communication/navigation providers, the meteorological service, maintenance providers/supervisor, and the Arctic environment are also represented externally. Ship and Shore site specialize the receiving-site concept.

Do not equate the entire service-provider organization with the automated system. Existing component choices, sensor types, aircraft configuration, and communication technology are not established by these function allocations.

## Mission and Capability Traceability

The model mission is `M1 Provide emergency medical supply in the Arctic`. Existing capability realization links connect:

| System capability | Operational capability |
| --- | --- |
| SC1 Deliver emergency medicine | OC1 |
| SC1.1 Deliver to a port or shore site | OC1.1 |
| SC1.2 Deliver to a ship at sea | OC1.2 |
| SC2 Operate legally and safely in shared air and sea space | OC2 |
| SC4 Acquire and share weather data during delivery | OC4 |
| SC5 Keep the service ready | OC5 Keep the service ready and funded |

The names and scope differ slightly for SC5/OC5; do not silently rename them. All six capability links exist, but full function/exchange traceability has not been validated.

## Delivery Cases and Existing Scenario

**SC1.2 — Ship:** Emergency report and treatment decision lead to a delivery request. Mission control accepts it; the system establishes contact with the receiving site and builds a route using ship position and forecasts. Approval precedes package loading and launch. During flight, live ship position, navigation signals, weather conditions, forecasts, and mission-control instructions support flight execution and replanning. The system reports flight status and weather data, then hands over the medicine.

**SC1.1 — Port or shore site:** The report describes shared delivery functions with a fixed destination, without the Ship actor and its position updates. A dedicated system architecture diagram exists, but a separate exchange scenario is not present.

The existing ship exchange scenario has 28 sequence messages and ends with package handover. The current sources do not establish detailed behavior for all abort/recovery cases or a complete post-handover return cycle. These are review questions rather than approved changes.

## Where to Look in Capella

- `[CSA] System Context` — Contextual system actors.
- `[MB] Missions` and `[MCB] Capabilities` — Mission and capability views.
- `[SAB] Delivery to a ship` and `[SAB] Delivery to a port` — System architecture diagrams showing functions, actors, and exchanges.
- `[SFBD] Root System Function` — System function breakdown diagram.
- `[ES] SC1.2 Deliver to a ship at sea` — Exchange scenario, showing interactions over time.

The SA layer contains 44 functions plus the root function, 42 functional exchanges, six capabilities, one mission, and one exchange scenario. It also contains 18 function-realization and 12 exchange-realization links. Counts include retained and decomposed elements; they are not a measure of validated completeness.

## Provisional Quantitative Inputs

For the current UAV comparison, use **312 km average nearest-candidate distance** and **approximately 630 km one-way reach for full coverage of the selected reference route**. Main shipping areas take priority; full coverage is optional. These geographical benchmarks do not replace or approve workbook requirements. See the [current technical requirements / agent brief](../System_Architecture/technical-requirements-brief.md), [coverage evidence](../Operational_Analysis/nsr-coverage-summary.md) and DEC-003 in the [decision log](../decision-log.md). The table below retains the historical source statements.

| Input | Existing statement | Evidence and status |
| --- | --- | --- |
| Delivery time | 4 hours overall versus 3 hours for shore sites / 5 hours for ships | Part 2 and workbook A4 conflict with Part 1; unresolved. |
| Payload | 3 kg | Part 2 and workbook B1; workbook status Open. |
| Package temperature | +2…+8 °C | Part 2 and workbook B3; workbook status Open. |
| Coverage | 300 km to a ship; 200 km to a fixed site | Workbook C2/C1 and Part 1; workbook statuses Open. |
| Operating conditions | −40…+20 °C; sustained wind up to 15 m/s | Part 2 and workbook D1/D2; workbook statuses Open. |
| Measurement performance | Range/accuracy for temperature, pressure, wind and visibility; sampling, altitude coverage, and data latency | Workbook F1–F7; proposed values with status Open. |

The workbook contains 55 questions: 54 Open, one Assumed, and none Confirmed during review. C3 (maximum target-ship speed) is blank. C4 (transit time) contains a formula with no cached result; that does not by itself show the formula is invalid. Do not present these inputs as approved requirements or independently verified facts.

## Next Work to Agree with the User

1. Resolve conflicting targets, identify supporting evidence, and select the authoritative workbook.
2. Review function allocations, scenario coverage, and traceability before treating SA as an approved baseline.
3. Use agreed functions and requirements to develop logical architecture (internal functional organization) for the current PDR goal. A completed physical architecture (implementation components) is not explicitly listed in the [user-provided PDR deliverables](../PDR/README.md); confirm expectations before extending that scope.

Keep overall progress in [status.md](../status.md), approved/proposed decisions in [decision-log.md](../decision-log.md), and unverified assumptions in [assumptions.md](../assumptions.md). Changes require the user's explicit authorization.

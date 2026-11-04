# Operational Analysis — Current State

Last reviewed: 2026-11-04.

Project: **Emergency drug delivery to a ship or port based on UAV system with inflight data acquisition: temperature, pressure, winds and visibility measurements**

## Status and Purpose

The user reports that Operational Analysis (OA) has been performed. The existing Capella model contains stakeholder groupings, operational capabilities, activities, and exchanges. This summary provides an entry point for future agents; it is not a formal approval or a complete model audit.

OA describes the people and organizations involved, what they need to achieve, and their interactions before allocating responsibilities to an automated system. The existing analysis considers Northern Sea Route and Arctic operations. Delivery and inflight weather-data acquisition are both part of the project scope.

## Source Files

- [Part 2 report, section 1](../../SE_my_notes/Problem%20set%202/Team5_problem2_part2.docx) — Explanation of the operational model.
- [Capella model, Operational Analysis layer](../Capella/UAV_Delivery_Arctic.capella) — Model elements and relationships.
- [Capella diagram file](../Capella/UAV_Delivery_Arctic.aird) — Diagram representations; retain alongside the `.capella` and `.afm` files.
- [Part 1 IDEF0 report](../../SE_my_notes/Problem%20set%202/Team5_problem2_part1.docx) — Complementary functional decomposition. Its A1–A5 labels are distinct from Capella operational identifiers.

The summaries explain existing material. Consult the model or report before making detailed engineering claims or edits.

## Stakeholders Already Modeled

The model contains seven top-level entity groups with more detailed stakeholders beneath them.

| Entity group | Existing role |
| --- | --- |
| UAV Service Provider | Plans and operates the delivery service, collects/processes weather data, manages supplies and permits; includes operator and maintenance-supervision roles. |
| Medical Chain | Medical coordinator decides treatment and orders delivery; pharmacy prepares medicine. |
| Receiving Site | Reports the emergency and receives the package; includes site supervisor, receiving crew, and patients who receive treatment. |
| Authorities | Port, aviation, and maritime authorities provide approvals and operating rules. |
| External Service Suppliers | Communication/navigation providers and maintenance companies support operations. |
| Customer & Funding | Shipping companies, meteorological service, industrial operators, and state health services are grouped as customers/funders. |
| Affected Public | Port workers, residents, and sea users can raise concerns about operations. |

These are existing model groupings, not evidence that stakeholder needs or commercial arrangements have been validated.

## Operational Capabilities

Preserve these identifiers and their existing numbering.

| ID | Existing capability |
| --- | --- |
| OC1 | Deliver emergency medicine. |
| OC1.1 | Deliver to a port or shore site; specialization of OC1. |
| OC1.2 | Deliver to a ship at sea; specialization of OC1. |
| OC2 | Operate legally and safely in shared air and sea space. |
| OC4 | Acquire and share weather data during delivery. |
| OC5 | Keep the service ready and funded. |

## Operational Flows

1. **Emergency delivery:** Receiving Site reports an emergency; the medical coordinator decides treatment; the pharmacy prepares the package; the provider plans delivery; Authorities approve it; the operator transports it; the receiving crew receives and confirms the package; treatment follows.
2. **Weather data:** The provider collects observations during delivery, processes and supplies the data, and the meteorological service uses them in forecasts. Forecasts feed back into delivery planning. Temperature, pressure, winds and visibility measurements are a second service output.
3. **Readiness and funding:** Customers/funders provide payment; the provider manages supplies; maintenance companies repair equipment; the maintenance supervisor inspects and releases equipment. Readiness status feeds planning.
4. **Safe and legal operation:** The provider applies for permits; Authorities issue permits and rules; Affected Public can raise concerns that feed the authority activity.

IDEF0 additionally decomposes the overall function into planning/launch (A1), carrying the package (A2), flying to the ship (A3), handover/confirmation (A4), and acquiring/sharing weather data (A5). It does not replace the operational stakeholder model.

## Where to Look in Capella

- `[OEBD] Stakeholder hierarchy` — Operational entity breakdown diagram: stakeholder hierarchy.
- `[OCB] Mission capabilities` — Operational capability diagram.
- `[OAB] Delivery`, `[OAB] Weather data`, `[OAB] Readiness`, and `[OAB] Safe and legal operation` — Operational activity diagrams: activities and their exchanges.

The OA layer currently contains 20 activities plus the root activity, 20 functional exchanges, and six capability elements including the two delivery specializations. These counts describe model content, not completeness.

## Handoff to System Analysis

The [System Analysis summary](../System_Analysis/README.md) explains how selected provider activities are allocated to the automated system while human mission control and other services remain external actors. All six operational capabilities have corresponding system-capability realization links, which record how the system capabilities implement the operational capabilities.

## Open Questions for Further Work

- Formal approval and full consistency checking of the operational model are not recorded.
- Quantitative performance values remain provisional; see the [project status](../status.md) for the delivery-time conflict and workbook status.
- Treat investor/buyer grouping and weather-data sales as existing modeling choices whose stakeholder evidence may need confirmation.
- Before extending this phase, agree the specific task with the user. Preserve identifiers and traceability; do not restart the analysis or silently introduce new requirements.

Project-wide decisions and assumptions belong in [decision-log.md](../decision-log.md) and [assumptions.md](../assumptions.md).

# Engineering Decision Log

Record engineering decisions and their rationale here. The current contextual review has not established a history of approved design decisions; an empty log does not mean that no decisions have been made.

The user-confirmed project title and scope are preserved in [README.md](README.md) and [project instructions](../AGENTS.md). Numerical values in the existing reports and workbook have not been recorded here as approved requirements.

Use stable identifiers starting with `DEC-001`. Status values: **Proposed**, **Approved**, or **Superseded**. Record user approval only when explicitly given. For a superseded decision, link to its replacement and retain the original entry.

| ID | Date proposed | Decision | Rationale and alternatives | Evidence / affected artifacts | Status | Approved by / date | Superseded by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DEC-001 | 2026-11-04 | Use straight-line distances for the initial relay-network geographical assessment; interpret them as geodesic surface distances between sourced coordinates. | The user explicitly accepted straight-line measurement. This is a screening method, not proof of operational flight range. | User confirmation in this conversation; [theory notes](Operational_Analysis/relay-network-theory.md). | Approved | User confirmed straight-line screening / 2026-11-04; computational interpretation documented for review. | — |
| DEC-002 | 2026-11-04 | Assess 300 km as one-way outward reach; drone lands on recipient ship and swaps its battery there. | User clarified this operating concept; it is not validated aircraft or ship capability. | User statements in this conversation; [coverage summary](Operational_Analysis/nsr-coverage-summary.md). | Approved | User confirmed concept / 2026-11-04 | — |

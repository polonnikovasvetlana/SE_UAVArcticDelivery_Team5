# Technical Requirements — UAV Range Study and Agent Brief

Updated: 2026-11-04.

Project: **Emergency drug delivery to a ship or port based on UAV system with inflight data acquisition: temperature, pressure, winds and visibility measurements**

## Problem and desired result

Identify realistic UAV solutions for emergency medicine delivery to ships or ports along the Northern Sea Route, while acquiring inflight temperature, pressure, winds and visibility measurements. Prioritize service to the main shipping areas. Complete geographical coverage is not mandatory. The user considers an extensive intermediate charging/relay network difficult to establish; compare aircraft and operating concepts that reduce reliance on new stations.

## Two distance benchmarks

| ID | Distance | Meaning and use |
| --- | --- | --- |
| RNG-001 | **312 km** | Length-weighted average of the distance from the studied shipping-route line to the nearest candidate launch site. Use as the average-distance planning benchmark for comparing useful one-way delivery reach. It is not a minimum aircraft range, demand-weighted average, or proof of coverage of most shipping activity. |
| RNG-002 | **Approximately 630 km** | One-way geographical reach sufficient for full coverage of the selected historical reference line under the existing candidate-site assumptions. Use as the optional full-reference-route scenario, not a mandatory service requirement or proof of coverage of every Northern Sea Route alternative. |

Evidence: [coverage summary](../Operational_Analysis/nsr-coverage-summary.md), its linked calculation outputs, and [DEC-003](../decision-log.md). These benchmarks supersede the earlier distance framing for this comparison brief. Historical workbook entries, relay calculations and maps retain their original values and status.

The main shipping sections, acceptable uncovered sections and required coverage percentage remain to be agreed. Do not infer them from the average. Candidate-site access, power and support remain unverified. Both distances are geographical references; actual flight feasibility must include route deviations, moving-ship interception, payload, wind, reserves and recovery.

## Working technical constraints

These inputs come from the existing workbook and architecture study; they are not a fully approved specification.

| Item | Working input / open issue |
| --- | --- |
| Payload | Approximately 3 kg. Confirm whether this includes the insulated container, sensors and landing equipment; account for their total mass and power. |
| Response time | Proposed 4 hours from emergency request to handover. Existing 3-hour shore / 5-hour ship statements conflict; report feasibility without silently choosing a final target. |
| Environment | Target ambient −40 to +20 °C; sustained wind 15 m/s and gusts 20 m/s in the architecture study. Check takeoff, cruise and landing limits separately; cold rating does not establish icing capability. |
| Medicine protection | Target +2 to +8 °C for 6 hours in the architecture study; verify packaging performance independently of ambient weather measurement. |
| Ship delivery | Current user-selected concept is vertical landing, crew unloading and battery replacement aboard the receiving ship. Moving-deck capability, compatible batteries and onward recovery remain unverified. |
| Aircraft mass | Earlier architecture assumes maximum takeoff weight at most 30 kg. Assess larger aircraft as explicitly identified alternatives; this is not approval to change the limit. |
| Energy | Compare battery, combustion-engine and hybrid aircraft. Fuel support or changes to battery-swap arrangements must be identified as proposed concept changes. |

Sources: [System Analysis](../System_Analysis/README.md), [requirements workbook](../Operational_Analysis/UAV_NFR_Questions.xlsx), [architecture study](Arctic_UAV_Decision_Tree_EN.pdf), [decision log](../decision-log.md) and [assumptions register](../assumptions.md).

## Task for the next agent

Compare available products and demonstrated solutions against RNG-001 and RNG-002, focusing on useful distance with the medical package and inflight measurement equipment installed. Consider aircraft retaining vertical ship landing, longer-range fixed-wing aircraft with alternative transfer/recovery, and larger fuel-powered or hybrid aircraft. Treat alternatives as proposals requiring user agreement.

For each candidate, provide payload-dependent flight range, cruise speed and mission time, temperature/wind limits, icing evidence, takeoff/landing method, ship compatibility and product maturity. Distinguish total flight distance, one-way delivery reach, return/recovery requirements and communication range. Separate manufacturer claims, demonstrated results and calculated estimates. Use current manufacturer documents and operational evidence, and flag unknown cost or procurement availability. Recommend the most credible options and identify which working constraints each would require changing. Do not assume that an aircraft can achieve all published maxima simultaneously.

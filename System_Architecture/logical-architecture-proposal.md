# Logical Architecture starting proposal

Reviewed: 2026-11-09. Status: proposed structure for discussion and implementation, not an approved architecture baseline.

## Sources and actual model state

The working source for this review is `../../UAV_Delivery_Arctic/`, as requested by the user. Its model and representations differ from the older repository copy in `../Capella/`. Do not overwrite either copy or transition from the older copy by accident.

- The parent-folder `.capella` header and `.afm` identify Capella **7.1.0**. This identifies the model version, not an independently checked running application version.
- Parent-folder SA contains **53 system functions including the root**, **49 functional exchanges**, six capabilities, and one exchange scenario. The repository copy contains 45 functions including the root and 42 exchanges.
- Parent-folder representations include `[SAB] Way back`, alongside delivery-to-ship, delivery-to-port, function-breakdown, context, mission and capability views.
- LA has only `Root Logical Function` and `Logical System`, with existing realization links to SA. No developed logical decomposition or LA diagrams were found.
- The SA system component is currently named `w`; its existing ID and links identify it as the system. It has 19 function allocations. Older summaries describing a component named `System` with 12 allocations describe the repository copy, not this working version.
- Reviewed the current, locally modified `Schemes/Schemes.drawio` and the supplied screenshot. The draw.io file also contains a broader medical-site/local-UAV/long-range-UAV/relay concept. That broader concept is a candidate extension, not a requirement to introduce two UAV classes now.

## Proposed component hierarchy

Keep the screenshot's organization, describing equipment and software responsibilities within the existing automated-system boundary:

```text
Logical System
  Station Support
  Control Center
    Mission Coordination
    Path Planning Module
  UAV
    Flight and Landing Control
    Communications and Status
    Medical Payload Management
    Weather Data Acquisition
  Destination Landing Support
```

Start with the four first-level components; introduce the children when allocating their functions requires the detail. The screenshot's Path Planning Module stays inside Control Center. Mission Coordination is the proposed home for automated return-site selection and readiness handling.

`Station Support` means system-owned equipment and software for checking, servicing and dispatching a UAV. `Destination Landing Support` means system-owned equipment/software assisting approach at the selected destination. They describe different roles in the cycle; one real installation may support both. They do not establish that infrastructure is installed at every candidate site or ship.

Human `Mission control` remains an external actor. Its approval, launch authorization and abort decisions are distinct from Control Center equipment/software. Receiving crew, maintenance personnel, authorities, medical chain and external service providers retain their existing external responsibilities. A geographical site or whole ship is not automatically an internal logical component.

## Function allocation starting point

Names in backticks below are the existing working-model SA names. Transition their functions and retain realization links before refining them in LA.

| Proposed logical owner | Existing SA functions / proposed refinement |
| --- | --- |
| Station Support | `Check the UAV`, `Recover the energy`, `Report that UAV is ready to fly`, `Request destination for return`. Separate automated diagnostics/energy servicing from human repair and battery handling where needed. |
| Control Center / Mission Coordination | Proposed refinements: evaluate current flights and station availability; select a suitable return destination; coordinate readiness and mission updates. These responsibilities appear in the sketch but have no separately named SA function yet. Review them against `Build initial route` and existing Mission control responsibilities before defining traceability. |
| Control Center / Path Planning Module | `Build initial route`; proposed ground-side refinement of `Replan the trajectory`. Separate strategic route planning from immediate onboard avoidance. |
| UAV / Flight and Landing Control | `Deliver`, `Land`; refine `Transport package to the site` through its existing children `Receive route and updates`, `Navigate and avoid obstacles`, `Optimyse the rout according to the weather`. Review overlap with the other route/flight functions before allocation. |
| UAV / Communications and Status | `Take updates from the mission control`, `Report flight status`, `Establish connection with a ship`, `Establish connection with destination`. Separate the onboard connection endpoint from the destination endpoint. |
| UAV / Medical Payload Management | `Take the medicine`, `Keep package temperature`, `Hand over package`. Keep these visible in delivery views even though the return sketch omits them. |
| UAV / Weather Data Acquisition | `Collect weather data on the way`, `Monitor and report the weather`; review overlap with `Measure the weather and send it out`, a child of `Transport package to the site`. Preserve temperature, pressure, winds and visibility acquisition. |
| Destination Landing Support | `Track landing` is currently system-owned and is a candidate for allocation here. Refine its support information separately from onboard landing execution. `Keep contact` is currently allocated to external Receiving Site: retain that actor behavior and introduce a distinct equipment endpoint if needed. |

Allocate executable leaf functions after refinement. Do not allocate the same undivided function to several components to represent a conversation: model the participating endpoint functions and their exchanges. Preserve SA identifiers; any change to SA responsibility or boundary needs an explicit, traceable revision.

## Return/redeployment flow matching the sketch

1. Station Support reports inspection and energy-service results, UAV readiness and a return/redeployment request.
2. Control Center selects a suitable destination using UAV energy/status, flight traffic and station availability. Availability and selection criteria are proposed detail, not verified infrastructure capability.
3. Path Planning Module generates the route; the human operator supplies the required authorization through the external Mission control interface.
4. UAV receives the route, executes it and reports position, energy, flight state and faults.
5. UAV establishes contact with Destination Landing Support and reports its approach. Destination support returns landing location/status, approach guidance and clearance information as applicable.
6. UAV executes landing and reports completion. Station support begins the next inspection/service cycle at the receiving installation.

Use named information or material exchanges instead of treating every arrow as a sequence instruction. Suggested interfaces: UAV readiness, servicing result, return request, selected destination, flight plan, authorization, telemetry, approach notice, landing guidance, landing clearance, landing completion. An exchange scenario records ordering, decisions and failure branches.

The SA model currently has eight exchanges named `-`, including the readiness chain and destination-contact/landing interactions. Define their actual contents during refinement. The screenshot also has a direct landing-to-checking loop, whereas the model has `Land` feeding `Hand over package`; these describe different mission contexts and should be reconciled through separate delivery and return views.

## Capella implementation sequence

1. Save the working project in Capella and preserve a backup of its `.capella`, `.aird` and `.afm` together before structural edits.
2. Review the existing SA functions and allocations, particularly the `w` system name, broad transport-function decomposition, unnamed exchanges and actor-owned `Keep contact`. Do not silently replace or rename existing elements.
3. Transition SA actors, relevant functions/exchanges and capabilities into the existing LA using Capella transitions. Check the resulting realization links and completeness; avoid manually creating disconnected copies of the SA functions.
4. Create `[LCBD] Delivery system structure` with the four first-level components and Path Planning Module nested in Control Center.
5. Create `[LAB] Return and redeployment`, arranged like the screenshot. Add the transitioned/refined logical functions, allocate them to the components, and show external Mission control where authorization is relevant.
6. Create `[LAB] Delivery to a ship` and `[LAB] Delivery to a port` using the same logical elements, including payload protection and weather acquisition. Keep ship position updates specific to the moving-destination case.
7. Name functional exchanges and define the component interfaces that carry exchanges across component boundaries. Add a return/redeployment functional chain and an exchange scenario for ordering and alternatives.
8. Run Capella validation and inspect missing realizations, unallocated executable functions, invalid exchange endpoints and inconsistent actor allocations. Review unavailable destination, insufficient energy, communication loss and landing rejection behavior without inventing approved performance thresholds.

The project's [referenced LA tutorial](https://gettingdesignright.com/GDR-Educate/Capella_Tutorial_v6_0/LogicalArchitecture.html) supports transitioning SA elements, creating an LCBD, allocating functions in LAB views and refining functional chains/scenarios. It targets Capella 6.0; exact menu labels must be checked in the installed 7.1.0 application.

This review changes no Capella model or draw.io source. It supplies a concrete starting structure while preserving the current delivery, weather-acquisition and human-operator boundary.

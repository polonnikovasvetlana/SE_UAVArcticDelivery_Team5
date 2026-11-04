# NSR one-way delivery coverage — first estimate

Updated 2026-11-04. Existing Arctic_relay_map PNG/PDF/SVG replaced at the user's request with 300 km circles and covered/uncovered route segments. Original Arc_map_full/local images remain reference inputs.

## Route and limits

[Arctic Sea Routes dataset](https://services1.arcgis.com/cc7nIINtrZ67dyVJ/ArcGIS/rest/services/Shipping_and_Hydrography/FeatureServer) credits NGA and describes its Northern Sea Route line as based on routes used by Russian icebreakers and cargo ships. This is a historical, generalized reference line, not a current navigational track, a complete collection of route alternatives, or an approved shipping corridor. Retrieved geometry is preserved in nsr-source-routes.json. The calculation selects the line from approximately 58°E at the Kara Sea entrance to the Bering Strait (66.69°N); western/southern approaches are excluded. Endpoints are dataset vertices, not surveyed legal boundaries.

## Results

- Selected reference length: approximately 4,675 km.
- Within 300 km of one of 57 candidate sites: approximately 2,186 km (46.8%).
- Beyond 300 km: approximately 2,489 km (53.2%).
- Length-weighted average nearest-site distance: 312 km. This is a uniform-along-route geometric average, not average distance per actual delivery.
- Maximum sampled nearest-site distance: 619.4 km near 77.79°N, 94.97°E (nearest candidate: Dikson).
- About 630 km nominal reach covers this selected line, allowing for the ≤5 km sampling interval. This is not an aircraft performance requirement or proof of coverage of every NSR route.

WGS84 geodesic circles have a 300 km radius. Route segments are interpolated with WGS84 geodesics and sampled at midpoints every ≤5 km. Route coverage percentages are length-weighted. The continuous-line maximum is bounded above by the sampled maximum plus 2.5 km. Raw calculations: nsr-coverage-results.json and nsr-coverage-samples.csv. Reproduce with create-relay-map.py (NumPy, Matplotlib and system PROJ).

## Operating assumptions

Current user direction (DEC-003): prioritize main shipping areas and accept incomplete coverage. Use **312 km** as the average nearest-candidate planning benchmark and **approximately 630 km** as the optional full-reference-line reach scenario. Do not call the average a minimum aircraft range or infer a share of actual delivery demand from it. The priority sections and acceptance percentage have not been defined. See the [technical requirements / agent brief](../System_Architecture/technical-requirements-brief.md). Existing map circles and calculation results remain the historical screening evidence.

The user specifies one-way delivery, landing on the recipient ship and swapping the battery there. Availability of all 57 candidate launch sites is optimistic: electricity, permanent support and access are not qualified everywhere. Compatible charged batteries, crew and landing arrangements on recipient ships remain unverified. Wind, payload, reserves, ship motion and recovery after the swap are not modeled. No shipping-corridor width is assumed, so no covered sea-area percentage is claimed. Weather-data acquisition during delivery remains part of the project scope; this map does not evaluate measurement coverage or accuracy.

Next: agree the priority shipping sections and acceptable uncovered portions, compare UAV capability against the two benchmarks, and qualify launch sites before using these numbers as service-wide coverage claims.

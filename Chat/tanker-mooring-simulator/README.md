# Tanker mooring simulator

## Input

A powerful browser-based simulator of a tanker moored at a berth or a single point mooring (SPM), built on three.js: 6-DOF hull motion under wind, current and waves, mooring lines with live tensions, fenders, and an interactive UI with parameter controls and charts. The simulator is this channel's output, a single self-contained page anyone can open. The build is run by the worker sub-channel [build](Chat/tanker-mooring-simulator/build/README.md).

## Output format

Website

## Guide

### Start and navigate

Open output/index.html in a modern WebGL browser, or serve this folder with a static HTTP server. Internet access is required for the exact pinned CDN dependencies (three.js 0.160.0, lil-gui 0.19.2, uPlot 1.6.31); there is no build step. Drag to orbit, scroll to zoom, and use Top, Side, Bow or Free orbit camera presets. Follow tracks the vessel. On narrow screens the controls continue below the scene.

### Scenarios and units

Choose Calm, Design storm, Passing ship surge (a prescribed transient centered around 35 seconds), or Line failure (first line releases at 15 seconds). Choose Berth or CALM SPM in Vessel. Aframax, Suezmax and VLCC presets represent approximately 110k, 160k and 300k DWT; displayed displacement is the actual model mass in tonnes. Ballast reduces draft and displacement and increases windage. Changing geometry or environmental controls restarts the run; reset restores the geometry and default line lengths while retaining the current environmental settings. JSON preserves edited line settings; it starts a new run rather than resuming a state snapshot.

All inputs use SI units, with line and fender displays in kN, angles in degrees, and displacement in tonnes. Directions describe force/wave propagation TOWARD: 0 degrees is +x along the berth, 90 degrees is +y toward the berth, and z is up. Positive roll, pitch and yaw follow right-hand rotations about x, y and z. Motion charts combine metres and degrees and are labeled in the chart tooltip. Their colors follow the label order shown when hovering over the chart area.

### Vessel and environment

The six-degree-of-freedom rigid hull uses diagonal mass/inertia and approximate added mass, linear plus quadratic damping, and hydrostatic heave, roll and pitch restoring. Waterplane coefficient controls heave stiffness; GM and GML control roll and pitch. Vessel controls show dimensions, displacement and windage. Wind and current use illustrative relative-angle drag fits in the style of OCIMF load decomposition, with yaw lever arms, deterministic multi-frequency gusts, a depth-averaged shear reduction, and an under-keel-clearance multiplier capped at three. These are not the proprietary vessel coefficient tables in MEG4.

Twenty-four seeded components approximate JONSWAP with significant height Hs, peak period Tp, gamma and uniform directional spreading. Physics and the ocean shader use identical component amplitude, frequency, direction and phase. Five by three waterplane strips approximate Froude-Krylov excitation with depth attenuation; the optional mean drift is a simple Hs-squared estimate. Added mass and damping are diagonal approximations, without diffraction, radiation memory, measured RAOs or full rigid-body gyroscopic coupling. Waves use deep-water dispersion even when water depth is small.

### Lines, winches and fenders

Open each Lines folder to choose elastic or catenary behavior, material, unstretched length, axial rigidity EA, submerged weight, MBL, compliant tail fraction and target pretension. Elastic lines carry tension only, with nonlinear strain hardening and a material/tail stiffness factor. Set pretension recalculates unstretched length at the current endpoint distance; for catenaries tune length to obtain the desired tension. Negative winch speed pays in, positive pays out. Brake threshold is percent of MBL; zero disables slip. Brake slip is rate limited and can still permit overload. Breakage above MBL is optional; Broken / release also manually releases a line. SWL defaults to 50% MBL; amber begins at SWL and red at 80% MBL. Every line shows tension and percent MBL.

Catenaries solve horizontal and vertical endpoint geometry with an elastic Newton iteration. Flat seabed contact uses a frictionless grounded-plus-suspended approximation; it omits grounded elasticity and soil friction. Cable inertia, bending, snap loading and dynamic touchdown are omitted. Elastic line curves are visual sag approximations; catenary curves follow the solved static shape. The CALM buoy has three translational degrees of freedom, drag, added mass and linear heave stiffness, with six chain legs; hawsers transfer force back to the buoy so the vessel can weathervane. Hawsers start slack in calm water; edit their length or pretension to tension them. Buoy rotations and detailed hydrostatics are omitted.

Berth lines include head, stern, breasts and springs. Fender precompression is initialized to balance lateral line pretension in the default symmetric geometry. Fenders use F = k delta^n, a compression dashpot and regularized Coulomb friction. Hover the fender-sum HUD for each fender's deflection, reaction and stored compression energy in kJ. This energy is the area under the reaction curve, not accumulated irreversible dissipation. Travel exceedance raises an alarm; the model does not include a rigid berth collision stop.

### Run, inspect and export

Space pauses/resumes, S advances one fixed step and pauses, R resets, and ? opens Help. Simulation controls set a fixed 0.005–0.04 second step and 0.25–20 times speed. A semi-implicit Euler accumulator decouples physics from rendering. Heavy workloads slow simulated time and raise a compute-budget message rather than increasing the step. Charts sample at up to 5 Hz and keep the latest 1,500 samples (about five simulated minutes). CSV exports this same rolling window. Save JSON and Load JSON round-trip configuration and per-line settings; load validates types and supported ranges. Max excursion and peak line tension (hover Max Line) reset with each run. Ocean resolution and capped pixel ratio bound rendering cost; frame rate depends on hardware.

### Validation and limits

Still-water berth equilibrium should remain at rest with symmetric line pretension balanced by fenders. CALM calm equilibrium starts with slack hawsers and balanced chain loads. A steady current should approach a steady offset with mean environmental load balanced by mooring, fender and damping forces; low damping can require a long settling period. Compare CSV trends, line loads and excursions before interpreting a run. Large rotations, very stiff short lines, severe forcing or extreme manual edits can invalidate the small-angle restoring and integration assumptions. Reset after such edits and compare results using a smaller fixed step.

This is an exploratory educational simulator, not a class-approved design tool, operational mooring assessment or substitute for site data and a qualified marine engineer. Coefficients, fender curves, line properties and buoy geometry are illustrative. Sources for the model structure are OCIMF Mooring Equipment Guidelines, fourth edition (2018), DNV-RP-C205 (2021), and the standard elastic catenary integrals dx/ds = H/T + H/EA and dz/ds = V/T + V/EA, with dV/ds = w. Consult the applicable current editions and validated vessel-specific coefficients for engineering work.

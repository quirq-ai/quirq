# Build the simulator

## Owner

sharmasuraj0123

## Worker

tanker-mooring-simulator/build

## Status

Done

## Input

Build a powerful, physically grounded, browser-based tanker mooring simulator on three.js in quirq-ai/quirq, and open one pull request against main.

**Where it goes.** quirq is a content repo with strict layout rules: read CONTRIBUTING.md and CLAUDE.md first. The simulator is the Website output of the channel `Chat/tanker-mooring-simulator/`, so it must be one self-contained file at `Chat/tanker-mooring-simulator/output/index.html` (inline CSS and JS; libraries from a CDN with exact pinned versions through an import map, e.g. three@0.160.0 from cdn.jsdelivr.net or unpkg; no build step, no other files in `output/`). It must run by opening the file or serving the folder statically. The README for the simulator is a `## Guide` section appended to `Chat/tanker-mooring-simulator/README.md` (keep its existing sections unchanged), plus an in-app Help panel with the same content. Don't add files anywhere else. `python3 .github/scripts/check_structure.py` must pass.

**Libraries.** three.js (WebGPU not required; WebGLRenderer) with OrbitControls, the three.js `Water` or a custom ocean shader, `Sky`, and `lil-gui` for parameter controls. Use uPlot or Chart.js for live time-series charts. Use any other small library that clearly helps (for example a seeded RNG). Keep the physics in plain JS, in its own clearly separated module section inside the file.

**Scenarios** (selectable in the UI):
1. Tanker alongside a jetty/berth: breast, spring, head and stern lines to bollards/quick-release hooks, with fenders between hull and berth.
2. Tanker at a CALM buoy SPM: bow hawser(s) to a buoy that is itself anchored with catenary chain legs, so the tanker weathervanes.
3. Optional: spread mooring.
Presets for vessel size (e.g. Aframax ~110k DWT, Suezmax ~160k, VLCC ~300k DWT) with realistic length, beam, draft, displacement, windage areas, and loaded/ballast condition.

**Physics.**
- Rigid-body 6-DOF hull (surge, sway, heave, roll, pitch, yaw) with mass, inertia tensor, added mass (approximate coefficients), linear plus quadratic damping, and hydrostatic restoring from waterplane area and GM/GML.
- Fixed physics time step (e.g. 0.02 s, configurable) decoupled from rendering, with an accumulator and a semi-implicit or RK4 integrator. Time scale control (pause, 0.25x to 20x), and a step button.
- Environment: wind (speed, direction, gusts via a spectrum such as API/NPD or a simple gust model) with OCIMF-style wind force and moment coefficients versus relative angle; current (speed, direction, optional depth profile) with OCIMF-style current coefficients and under-keel-clearance effect; waves as a JONSWAP or Pierson-Moskowitz spectrum (Hs, Tp, gamma, direction, spreading) summed from components, with first-order wave excitation from a simple strip or Froude-Krylov approximation and an optional mean wave drift force. The rendered sea surface must use the same wave components as the physics.
- Mooring lines: selectable per line between an elastic (nonlinear stretch, e.g. HMPE/polyester/nylon with tail, MBL, pretension) and a catenary model (chain or wire, weight per metre, seabed contact, solved per step, e.g. Newton iteration on the elastic catenary equations). Lines are slack in compression. Show each line's tension, % of MBL, and colour it green/amber/red against the safe working load (e.g. 50% MBL) with alarms. Lines can break when tension exceeds MBL, and winch pay-in/pay-out and brake slip are adjustable.
- Fenders: nonlinear reaction-deflection curves (e.g. pneumatic or cone fender), friction, and energy absorbed; show reaction force and deflection.
- Berth or SPM geometry with bollards, hooks, and water depth.

**UI.**
- 3D scene: hull with a reasonable tanker shape (procedural geometry is fine), deck and superstructure, lines drawn as catenary curves updated each frame, fenders, jetty or buoy, seabed, sky, and ocean. Camera presets (top, side, bow, free orbit) and follow mode.
- lil-gui panels for every parameter above, grouped (Vessel, Environment, Lines, Fenders, Simulation), with save/load of scenarios as JSON and a few built-in scenarios (calm, design storm, passing ship surge, line failure).
- Live charts: tension per line, 6-DOF motions (surge, sway, yaw, heave, roll, pitch), fender reactions, and environment, with a rolling window. A HUD with time, max tensions, max excursions, and alarms. Export the time series to CSV.
- Clear units (SI, tension in kN or t), keyboard shortcuts, and responsive layout. Keep 60 fps on a mid-range laptop.

**Quality.** Comment the physics with the equations and sources used (OCIMF MEG4, DNV-RP-C205, standard catenary equations). Sanity check: in still water with no wind the vessel stays at rest with pretensions balanced; a steady current gives a steady offset whose line tensions roughly balance the current force. Verify the page loads in headless Chromium without console errors before opening the PR.

Open one pull request against main titled "Add tanker mooring simulator", describing the model, its assumptions, and its limits. If you cannot push or create the branch, reply with the full contents of every file you changed so they can be applied by hand.

## Output format

GitHub URL

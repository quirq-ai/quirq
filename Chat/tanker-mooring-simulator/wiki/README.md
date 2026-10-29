# Simulator wiki

## Owner

sharmasuraj0123

## Worker

tanker-mooring-simulator/wiki

## Status

Done

## Input

Write a wiki that explains the tanker mooring simulator (Mooring Lab) in quirq-ai/quirq, and open one pull request against main titled "Add tanker mooring simulator wiki".

**Read first.** quirq is a content repo with strict layout rules: read CONTRIBUTING.md and CLAUDE.md. The simulator is `Chat/tanker-mooring-simulator/output/index.html` (read all of it, especially the physics section, the lil-gui controls, presets and scenarios, the HUD, charts and exports) and its guide is the `## Guide` section of `Chat/tanker-mooring-simulator/README.md`. The wiki must describe what the code actually does: check every parameter name, default, range, unit, preset value and keyboard shortcut against the code, and never invent features.

**Where it goes.** The wiki is the Website output of this sub-channel: one self-contained file at `Chat/tanker-mooring-simulator/wiki/output/index.html`, with all CSS and JS inline and no external requests at all (no CDN, no web fonts, no images from the web), so it opens offline and renders anywhere. Change no other file except this sub-channel's `chat.log.jsonl` if useful. `python3 .github/scripts/check_structure.py` must pass.

**Shape.** A wiki of separate pages inside that one file: a left sidebar listing the pages, one page shown at a time, switched by URL hash (`#overview`, `#concepts`, ...) so each page can be linked, with previous/next links at the bottom of each page, a search box that filters the sidebar, and a print style that prints all pages. Write the page content as clean semantic HTML (headings, short paragraphs, tables, lists, `<figure>` with inline SVG diagrams). Light and dark themes via `prefers-color-scheme`, readable on a phone (sidebar collapses), no horizontal scroll. Plain, precise language for a reader who is technical but not a mooring engineer.

**Pages.**
1. **Overview.** What Mooring Lab is, who it is for, what you can learn from it, and what it is not (an educational, exploratory tool, not a class-approved design or operational assessment tool). A quick start: open the page, pick a scenario, press play, watch line tensions.
2. **Tanker mooring concepts.** Why tankers are moored and what goes wrong. Vessel classes (Aframax, Suezmax, VLCC) with size ranges. Jetty/berth mooring versus single point mooring (CALM buoy SPM) and weathervaning. Line types by role (head, stern, breast, spring) with an SVG plan-view diagram of a berth layout. Fenders and what they do. The six degrees of freedom (surge, sway, heave, roll, pitch, yaw) with an SVG diagram of the axes and the sign convention the simulator uses. Environmental loads: wind, current, waves, passing ships. Safe working load, MBL and why lines are kept well below MBL.
3. **Mooring lines in depth.** Elastic versus catenary lines: when each applies, the equations used (tension-only elastic with strain hardening; elastic catenary dx/ds = H/T + H/EA, dz/ds = V/T + V/EA, dV/ds = w, solved by Newton iteration, with seabed contact), materials (HMPE, polyester, nylon, wire, chain) and compliant tails, pretension, winches, brakes and brake slip, line breakage and release. An SVG of a catenary with touchdown point.
4. **Fenders.** The reaction law F = k δ^n, compression damping, friction, energy absorption (area under the curve), travel limits and alarms.
5. **Environment model.** Wind and current loads (OCIMF-style coefficient fits versus relative angle, yaw moments, gusts, current shear, under-keel clearance factor), waves (JONSWAP with Hs, Tp, gamma, directional spreading; 24 components shared by the physics and the ocean shader; Froude-Krylov strip excitation; mean drift), and the passing ship transient. Direction conventions.
6. **Physics model.** The equations of motion of the 6-DOF rigid hull: mass and inertia, added mass, linear and quadratic damping, hydrostatic restoring from waterplane area, GM and GML, the CALM buoy model, the fixed-step semi-implicit Euler integrator with an accumulator, time scaling, and the compute-budget behaviour. Show the key equations (in readable HTML/Unicode, no MathJax).
7. **Using the simulator.** The UI tour: 3D view and camera presets and follow mode, every lil-gui folder (Vessel, Environment, Lines, Fenders, Simulation and any others) with a table of each control, its unit, default and range, the HUD, alarms and colours, keyboard shortcuts, and the Help panel.
8. **Scenarios and presets.** Each built-in scenario (Calm, Design storm, Passing ship surge, Line failure) and berth versus CALM SPM: what it sets up, what to watch, and what a learner should notice. Vessel presets with their actual model values (length, beam, draft, displacement, windage) and loaded versus ballast. Three or four guided experiments (for example: increase current and watch the offset and spring line loads; switch a line from polyester to nylon; break a line; compare berth and SPM in the same storm).
9. **Outputs and exports.** The live charts (what each shows, sampling rate, rolling window), max excursion and peak tension, CSV export (columns and units, with an example header), and JSON save/load (what is preserved and validated).
10. **Assumptions and limits.** Everything the model simplifies or omits, and when results become invalid (large rotations, stiff short lines, severe forcing, step size), with advice on checking a run. Sources: OCIMF Mooring Equipment Guidelines 4th edition (2018), DNV-RP-C205 (2021), standard catenary theory.
11. **Glossary.** At least 40 terms, alphabetical, each one or two sentences: added mass, Aframax, bollard, breast line, brake holding capacity, CALM buoy, catenary, compliant tail, current coefficient, damping, DWT, EA, fender, Froude-Krylov force, GM, GML, gust, hawser, heave, Hs, JONSWAP, MBL, mean drift force, OCIMF, pitch, pretension, quick-release hook, roll, SPM, spring line, SWL, surge, sway, touchdown point, Tp, UKC, VLCC, weathervaning, windage, winch, yaw, and more as needed.

**Quality.** Verify the page in headless Chromium: it loads with no console errors and no network requests, every sidebar link and hash route works, previous/next links work, search filters, and it renders at 390 px and 1440 px wide without horizontal scroll. Check every factual statement about the simulator against the code.

**Handing back.** Open the pull request against main describing the pages. If you cannot push or create the branch (a 403 from GitHub), do not stop: run `cd /path/to/repo && tar czf /tmp/wiki.tgz Chat/tanker-mooring-simulator/wiki/output/index.html && base64 -w0 /tmp/wiki.tgz > /tmp/x.b64 && wc -c /tmp/x.b64 && sha256sum /tmp/wiki.tgz`, then print `/tmp/x.b64` in pieces with one `cut -c` command per 1200 characters (for example `cut -c 1-1200 /tmp/x.b64`, `cut -c 1201-2400 /tmp/x.b64`, ...) until the whole file is printed, and say in your result that the files are in those outputs.

## Output format

Website

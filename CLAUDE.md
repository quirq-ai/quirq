# CLAUDE.md

This repository is a content workspace read by open-chat, not an application. Follow [CONTRIBUTING.md](CONTRIBUTING.md); it is the source of truth for layout, naming, and formats.

Before committing, run `python3 .github/scripts/check_structure.py` and fix everything it reports. Do not weaken the checker to make a change pass; if a rule needs to change, update the rule, the checker, and CONTRIBUTING.md together.

The short version:

- Top level holds only the five sections (`Activity`, `Chat`, `Insights`, `Library`, `Vision`), `.github/`, and the root docs and config files.
- Sections are flat and hold one file type each: Activity `.jsonl`, Chat `.json`, Insights `.json`, Library `.url`, Vision `.md`. Each has a `README.md`.
- Content file names are lowercase kebab-case.
- Links use paths relative to the repository root and must point to real files. No machine-specific paths.
- Scripts and tooling go under `.github/`, never in content folders.
- No generated files, logs, secrets, or duplicate copies.

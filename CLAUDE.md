# CLAUDE.md

This repository is a content workspace read by open-chat, not an application. Follow [CONTRIBUTING.md](CONTRIBUTING.md); it is the source of truth for layout, naming, and formats.

Before committing, run `python3 .github/scripts/check_structure.py` and fix everything it reports. Do not weaken the checker to make a change pass; if a rule needs to change, update the rule, the checker, and CONTRIBUTING.md together.

The short version:

- Top level holds only the five sections (`Activity`, `Chat`, `Insights`, `Library`, `Vision`), `.github/`, and the root docs and config files.
- Sections hold one file type each: Activity `.jsonl`, Chat `.json` (plus channel READMEs, inputs, and outputs), Insights `.json`, Library `.url`, Vision `.md`. Each has a `README.md`.
- Sections are flat except Chat, which is made of channels: `Chat/<channel>/` (a workstream, or a personal channel named after a GitHub login). A channel holds `README.md` (`## Input` and `## Output format`), conversations `*.json` (plus the hub's `*.log.jsonl` chat logs beside them), `inputs/` (any file type), and `output/`.
- A channel can hold sub-channels one level deep (`Chat/<channel>/<sub-channel>/`, same shape, README adds `## Owner`): worker threads a person or agent opens. Optional `## Status` is Open or Done.
- Keep channels few and messages many: reply in place, extend a channel before opening one, merge channels with the same output, mark finished ones Done, and fold finished sub-channels into their parent. Replies follow "How euler replies" in CONTRIBUTING.md: answer, what changed (links), next step.
- Output format is exactly one of Slides, One pager, Website, GitHub URL, and decides the output file: `output/slides.md`, `output/one-pager.md`, `output/index.html`, or `output/github.url`.
- Files dropped directly in `Chat/` are the inbox. Sort each into the best-fitting channel's `inputs/`, open a channel only when none fits, and regenerate changed outputs.
- When asked to work on a channel: read its README input, its conversations, and `inputs/`, then generate the output in the declared format.
- The repo is also `quirq/quirq` on hub.quirq.dev, which is the source of truth. Reply to hub chats directly on the hub; keep GitHub `main` the same as the hub's (see CONTRIBUTING.md, The hub).
- Content file names are lowercase kebab-case.
- Links use paths relative to the repository root and must point to real files. No machine-specific paths.
- Scripts and tooling go under `.github/`, never in content folders.
- No generated files, logs, secrets, or duplicate copies.

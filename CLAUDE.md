# CLAUDE.md

This repository is a content workspace read by open-chat, not an application. Follow [CONTRIBUTING.md](CONTRIBUTING.md); it is the source of truth for layout, naming, and formats.

Before committing, run `python3 .github/scripts/check_structure.py` and fix everything it reports. Do not weaken the checker to make a change pass; if a rule needs to change, update the rule, the checker, and CONTRIBUTING.md together.

The short version:

- Top level holds only the five sections (`Activity`, `Chat`, `Insights`, `Library`, `Vision`), `.github/`, and the root docs and config files.
- Sections hold one file type each: Activity `.jsonl`, Chat `.json` (plus task READMEs and outcomes), Insights `.json`, Library `.url`, Vision `.md`. Each has a `README.md`.
- Sections are flat except Chat, which is `Chat/<username>/tasks/<task-name>/` (username = GitHub login, lowercase). A task folder holds `README.md` (`## Goal` and `## Output format`), `chats/*.json` (plus the hub's `chats/*.log.jsonl` chat logs beside them), `sources/` (any file type), and `outcome/`.
- Output format is exactly one of Slides, One pager, Website, GitHub URL, and decides the outcome file: `outcome/slides.md`, `outcome/one-pager.md`, `outcome/index.html`, or `outcome/github.url`.
- Files dropped directly in `Chat/<username>/` are the inbox. Triage them per CONTRIBUTING.md: sort each into the best-fitting task's `sources/` (or `chats/`), create a task only when none fits, merge overlapping tasks so there are as few as possible, append new project-thread messages to the task's existing chat file, regenerate changed outcomes, then PR and merge on green CI.
- When asked to work on a task: read its README goal and everything in `chats/`, generate the outcome in the declared format, and save the conversation to `chats/` if it isn't there yet.
- The repo is also `quirq/quirq` on hub.quirq.dev. After merging to GitHub `main`, keep the hub's `main` the same (see CONTRIBUTING.md, The hub).
- Content file names are lowercase kebab-case.
- Links use paths relative to the repository root and must point to real files. No machine-specific paths.
- Scripts and tooling go under `.github/`, never in content folders.
- No generated files, logs, secrets, or duplicate copies.

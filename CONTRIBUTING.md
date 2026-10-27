# Keeping quirq organized

This repository is content for open-chat, not code. The app reads these files directly, so the layout below is the contract. `.github/scripts/check_structure.py` enforces every rule marked **(checked)**, and the Structure workflow runs it on each pull request and on pushes to `main`.

Run it locally before you push:

```sh
python3 .github/scripts/check_structure.py
```

## Layout

```
README.md          what the workspace is and how to open it
LICENSE
CONTRIBUTING.md    these rules
CLAUDE.md          the same rules, pointed at for AI assistants
.github/           CI and tooling (kept out of the content folders)
Activity/          feed events, *.jsonl
Chat/              saved conversations, *.json
Insights/          insight collections, *.json
Library/           web shortcuts, *.url
Vision/            direction documents, *.md
```

- Only the files and folders above may sit at the top level. **(checked)** A new section or top-level file needs this list, the checker, and the README updated in the same pull request.
- Every section has a `README.md` that says what goes in it. **(checked)**
- Sections are flat: no subfolders. **(checked)**
- Each section holds only its own file type, listed above. **(checked)**
- Tooling, scripts, and schemas live under `.github/`, never in the content folders or at the top level, so the app does not show them.

## Naming

- Section folders are Title Case and fixed: `Activity`, `Chat`, `Insights`, `Library`, `Vision`.
- Content files are lowercase kebab-case with a lowercase extension, such as `weekly-review.md` or `team-retro.json`. **(checked)**
- Name a file for what it holds, not when or by whom it was made. Avoid `new`, `final`, `copy`, `v2`, or dates in names; git keeps the history.
- `index.json` in Chat and Insights and `example.*` elsewhere are the names open-chat currently opens by default. Keep them until the app's conventions change.

## File formats

All files **(checked)**: UTF-8 without a byte order mark, LF line endings, a final newline, not empty, and under 1 MB. `.editorconfig` and `.gitattributes` set this up for most editors.

| Section | Format | Required **(checked)** |
| --- | --- | --- |
| Activity | JSON Lines, one object per line | `author`, `type`, `title`, `content` as strings on every record |
| Chat | JSON object | `"type": "conversation"`, string `title`, non-empty `messages` with `role` of `user` or `assistant` and string `content` |
| Insights | JSON object | `"type": "collection"`, string `title`, non-empty `items`, each with a string `title` |
| Library | Plain text | exactly one `http://` or `https://` URL |
| Vision | Markdown | starts with a `# Title` heading |

Every Markdown file, including the READMEs, starts with a `# Title` heading. **(checked)**

## Links

- Link between files with paths relative to the repository root, such as `Vision/example.md`. **(checked: every `path` in Chat and Insights must point to a file that exists)**
- Never write a path that only exists on one machine, such as a drive letter or a home folder. **(checked)**
- When you rename or move a file, update everything that links to it in the same pull request.

## What does not belong here

- Generated output, logs, exports, and build artifacts.
- Secrets, API keys, and `.env` files. App settings stay in open-chat's own `.env.local`.
- Duplicate copies of a file; edit the original instead.
- Notes about past cleanups or history; that belongs in commit messages.

## Changes

- Work on a branch and open a pull request into `main`; the Structure check must pass before merging.
- Keep one purpose per pull request, and describe what changed in the commit message.
- If a rule gets in the way, change the rule, the checker, and this file together in one pull request rather than working around it.

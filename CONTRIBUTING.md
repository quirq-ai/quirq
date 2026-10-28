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
Chat/              tasks: Chat/<username>/tasks/<task-name>/ (goal, chats, outcome)
Insights/          insight collections, *.json
Library/           web shortcuts, *.url
Vision/            direction documents, *.md
```

- Only the files and folders above may sit at the top level. **(checked)** A new section or top-level file needs this list, the checker, and the README updated in the same pull request.
- Every section has a `README.md` that says what goes in it. **(checked)**
- Sections are flat: no subfolders, except Chat (below). **(checked)**
- Each section holds only its own file type, listed above, plus README.md files. **(checked)**

### Chat: goal, chats, outcome

Chat is where work happens. Each task gets a folder, grouped by person:

```
Chat/
  README.md
  <username>/
    <any file>        inbox: drop anything here; Claude sorts it into a task
    tasks/
      <task-name>/
        README.md     "# Title", then "## Goal" and "## Output format"
        chats/        saved conversations about the task, *.json (+ *.log.jsonl)
        sources/      files sorted in from the inbox, any type
        outcome/      what Claude generated, in the task's output format
```

The workflow:

1. **Define the goal.** The person creates the task folder and writes the README: a `## Goal` section in their own words and a `## Output format` section.
2. **Store the chats.** Project conversations about the task are saved to `chats/` as conversation JSON (same format as below), one file per conversation, named for what it covers, such as `kickoff.json`.
3. **Generate the outcome.** Claude reads the goal, the chats, and the sources and writes the result to `outcome/`, then opens a pull request. When any of them change, Claude regenerates the outcome.

### Triage: sorting the inbox into fewer tasks

Anyone can drop files of any type and name straight into `Chat/<username>/`. Claude runs triage on a schedule and whenever asked:

1. **Sort.** Read each inbox file and move it (`git mv`) into the `sources/` of the task whose goal it serves, renamed to lowercase kebab-case. A saved conversation goes to `chats/` instead.
2. **Create only when nothing fits.** If no task fits, start one: draft the Goal from the file and pick the closest output format, and say in the Goal that Claude drafted it so the person can edit it.
3. **Consolidate.** Prefer fewer tasks. When two tasks' goals overlap or one is a step of another, merge them into the broader one: move its chats and sources across, combine the goals, and delete the emptied folder. Never merge goals the person wrote that are clearly separate.
4. **Chain the conversation.** Append the project thread's new messages to that task's existing `chats/` file for the thread rather than starting a new file each time. Turns people typed on the hub are already chained in that conversation's `.log.jsonl`.
5. **Regenerate** the outcome of every task that changed.
6. **Ship and report.** Open a pull request, merge it once the Structure check is green, and post what moved where in the project thread.

The checker lists inbox files as a note, not an error, so dropping files never breaks CI.

The output format decides the outcome file. These four are the only accepted formats:

| Output format | Outcome file | Must contain **(checked)** |
| --- | --- | --- |
| Slides | `outcome/slides.md` | Markdown starting with `# Title`, slides separated by a line of `---` |
| One pager | `outcome/one-pager.md` | Markdown starting with `# Title` |
| Website | `outcome/index.html` | A complete, self-contained HTML page |
| GitHub URL | `outcome/github.url` | Exactly one `https://github.com/` URL |

Rules:

- `<username>` is the person's GitHub login in lowercase. **(checked: lowercase kebab-case)**
- `<task-name>` describes the task in lowercase kebab-case, such as `plan-q4-launch`. **(checked)**
- Every task folder has a README.md with a `## Goal` section that has text under it. **(checked)**
- The README has a `## Output format` section whose first line is exactly one of `Slides`, `One pager`, `Website`, `GitHub URL` (case-insensitive). **(checked)**
- `outcome/` holds only the file for the task's format, and it may be absent until the outcome is generated. **(checked)**
- Inbox files directly under `Chat/<username>/` and files in `sources/` can be any type up to 25 MB. Sorted `sources/` files use lowercase kebab-case names. **(checked)**
- A conversation can have a chat log beside it: `chats/<name>.log.jsonl` next to `chats/<name>.json`. The hub's chat box writes it (see README), one turn per line, each a JSON object with `role` of `user` or `assistant` and string `content` (plus optional `id`, `author`, `time`, `links`). Leave these logs where they are and append to them rather than folding turns back into the `.json`. **(checked: matching `.json` exists, every line is a valid turn, link paths exist)**
- A task folder holds only README.md, `chats/*.json` and their `*.log.jsonl`, `sources/`, and `outcome/`. Nothing else goes in Chat: no files directly under `Chat/<username>/` or `tasks/`, and no deeper folders. **(checked)**

Example task README:

```markdown
# Plan Q4 launch

## Goal

Agree on the launch date, owners, and the three announcements.

## Output format

Slides
```

- Tooling, scripts, and schemas live under `.github/`, never in the content folders or at the top level, so the app does not show them.

## Naming

- Section folders are Title Case and fixed: `Activity`, `Chat`, `Insights`, `Library`, `Vision`. Folders inside Chat are lowercase kebab-case.
- Content files are lowercase kebab-case with a lowercase extension, such as `weekly-review.md` or `team-retro.json`. **(checked)**
- Name a file for what it holds, not when or by whom it was made. Avoid `new`, `final`, `copy`, `v2`, or dates in names; git keeps the history.
- `index.json` in Insights and `example.*` in Activity, Library, and Vision are the names open-chat currently opens by default. Keep them until the app's conventions change.

## File formats

All files **(checked)**: UTF-8 without a byte order mark, LF line endings, a final newline, not empty, and under 1 MB. `.editorconfig` and `.gitattributes` set this up for most editors.

| Section | Format | Required **(checked)** |
| --- | --- | --- |
| Activity | JSON Lines, one object per line | `author`, `type`, `title`, `content` as strings on every record |
| Chat (`chats/*.json`) | JSON object | `"type": "conversation"`, string `title`, non-empty `messages` with `role` of `user` or `assistant` and string `content` |
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

## The hub

The same repository is the project `quirq/quirq` on [hub.quirq.dev](https://hub.quirq.dev/quirq/quirq), in the `quirq` space. GitHub (`quirq-ai/quirq`) is where pull requests and the Structure check run; the hub is where the workspace is viewed and chatted in. Keep the two `main` branches the same:

- After a pull request merges, push `main` to the hub: `git push quirq main`.
- The hub's chat box commits straight to the hub's `main`. Before pushing, `git pull --no-rebase quirq main` so those commits come along without rewriting GitHub history, then push them to GitHub too.

## Changes

- Work on a branch and open a pull request into `main`; the Structure check must pass before merging.
- Keep one purpose per pull request, and describe what changed in the commit message.
- If a rule gets in the way, change the rule, the checker, and this file together in one pull request rather than working around it.

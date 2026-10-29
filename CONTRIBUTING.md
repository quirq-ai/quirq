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
Chat/              channels: Chat/<channel>/ (input, conversation, output)
Insights/          insight collections, *.json
Library/           web shortcuts, *.url
Vision/            direction documents, *.md
```

- Only the files and folders above may sit at the top level. **(checked)** A new section or top-level file needs this list, the checker, and the README updated in the same pull request.
- Every section has a `README.md` that says what goes in it. **(checked)**
- Sections are flat: no subfolders, except Chat (below). **(checked)**
- Each section holds only its own file type, listed above, plus README.md files. **(checked)**

### Chat: channels with an input and an output

Chat is where work happens. It is made of channels: each open workstream is one, and anyone can have a personal channel named after their GitHub login.

```
Chat/
  README.md
  <any file>          inbox: drop anything here; Claude sorts it into a channel
  <channel>/
    README.md         "# Title", then "## Input" and "## Output format"
    chat.json         the conversation (+ chat.log.jsonl from the hub's chat box)
    inputs/           files for this channel, any type
    output/           what Claude produced, in the channel's output format
```

The flow is input, then action, then output:

1. **Input.** Whoever opens the channel writes the README: an `## Input` section saying what is asked, and an `## Output format` section.
2. **Action.** People talk in the channel's conversation and drop files into `inputs/`. A channel can hold more than one conversation (`<name>.json`), but most need only `chat.json`.
3. **Output.** Claude reads the input, the conversations and the inputs, and writes the result to `output/`. When any of them change, Claude regenerates it.

Files dropped straight into `Chat/` are the inbox. Claude moves each into the `inputs/` of the channel it serves, renamed to lowercase kebab-case, and opens a new channel only when none fits. The checker lists inbox files as a note, not an error.

The output format decides the output file. These four are the only accepted formats:

| Output format | Output file | Must contain **(checked)** |
| --- | --- | --- |
| Slides | `output/slides.md` | Markdown starting with `# Title`, slides separated by a line of `---` |
| One pager | `output/one-pager.md` | Markdown starting with `# Title` |
| Website | `output/index.html` | A complete, self-contained HTML page |
| GitHub URL | `output/github.url` | Exactly one `https://github.com/` URL |

Rules:

- `<channel>` is lowercase kebab-case, such as `plan-q4-launch`. A personal channel is the person's GitHub login in lowercase. **(checked)**
- Every channel has a README.md with an `## Input` section that has text under it. **(checked)**
- The README has a `## Output format` section whose first line is exactly one of `Slides`, `One pager`, `Website`, `GitHub URL` (case-insensitive). **(checked)**
- `output/` holds only the file for the channel's format, and it may be absent until the output is generated. **(checked)**
- Inbox files directly under `Chat/` and files in `inputs/` can be any type up to 25 MB. `inputs/` files use lowercase kebab-case names. **(checked)**
- A conversation can have a chat log beside it: `<name>.log.jsonl` next to `<name>.json`. The hub's chat box writes it (see README), one turn per line, each a JSON object with `role` of `user` or `assistant` and string `content` (plus optional `id`, `author`, `time`, `links`). Append to these logs rather than folding turns back into the `.json`. **(checked: matching `.json` exists, every line is a valid turn, link paths exist)**
- A channel holds only README.md, conversations and their logs, `inputs/`, and `output/`. No deeper folders. **(checked)**

Example channel README:

```markdown
# Plan Q4 launch

## Input

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
| Chat (conversation `*.json`) | JSON object | `"type": "conversation"`, string `title`, non-empty `messages` with `role` of `user` or `assistant` and string `content` |
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

The same repository is the project `quirq/quirq` on [hub.quirq.dev](https://hub.quirq.dev/quirq/quirq), in the `quirq` space. The hub is the source of truth: it is where the workspace is viewed and chatted in, and its chat box commits straight to its `main`. GitHub (`quirq-ai/quirq`) mirrors it and runs the Structure check.

- Replies to hub chats are committed and pushed straight to the hub's `main`, not through GitHub pull requests.
- Before pushing anything to the hub, `git pull --no-rebase quirq main` so new chat turns come along. Never force-push the hub.
- Bring GitHub `main` up to the hub's `main` with a merge, so both stay the same.

## Changes

- Work on a branch and open a pull request into `main`; the Structure check must pass before merging.
- Keep one purpose per pull request, and describe what changed in the commit message.
- If a rule gets in the way, change the rule, the checker, and this file together in one pull request rather than working around it.

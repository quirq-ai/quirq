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
    <sub-channel>/    a worker thread: same shape, plus "## Owner" in its README
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
- A channel holds only README.md, conversations and their logs, `inputs/`, `output/`, and sub-channels. A sub-channel has the same shape but cannot hold sub-channels of its own, so Chat is at most two channel levels deep. **(checked)**
- A sub-channel's README also has an `## Owner` section naming who opened it: a GitHub login or an agent name, such as `euler`. Its parent channel must have a README. **(checked)**
- A sub-channel run by a worker agent has a `## Worker` section with text under it: the title of the Agents Hub task that runs it. **(checked)**
- Any channel README may have a `## Status` section whose first line is `Open` or `Done`. No section means Open. **(checked)**
- An agent's own channel has an `## Agent` section naming the agent, and is the top-level channel of the same name, like a personal channel. **(checked)**

Example channel README:

```markdown
# Plan Q4 launch

## Input

Agree on the launch date, owners, and the three announcements.

## Output format

Slides
```

### Working in channels

The goal is many messages in few channels: conversation should be rich, and the channel list short. People and agents both start work, so the same rules apply to both.

**Sub-channels are worker threads.** When part of a channel's work needs its own output, whoever takes it on (a person or an agent) opens `Chat/<channel>/<sub-channel>/` with an `## Owner`, an `## Input` scoped to that piece, and an `## Output format`. The owner works there and writes the output. The parent channel's output links to or folds in each sub-channel's output, so the parent stays the one place to see the whole workstream. A personal channel is where someone manages their own workers: its sub-channels are the threads they or their agents run.

**Every connected agent has a channel.** Each agent connected to the `quirq` space on the hub (see `spacehub agent list quirq`) gets `Chat/<agent>/`, opened automatically by `.github/scripts/sync_agent_channels.py`. Its README has `## Agent`, and its chat shows the agent's status (where it is connected and running) and the commits it pushes here, so you can watch it and talk to it in one place. `output/one-pager.md` is its profile and recent activity. When an agent disconnects, its channel is kept and set to Done; it reopens if the agent returns. euler runs the sync on each reply run and commits the result with the subject prefix `agent-channels:`. Do not edit the status or activity turns by hand; talk below them.

**Worker agents are Agents Hub tasks.** The workers are tasks on the Agents Hub: each runs in its own sandbox and can work on GitHub. A worker sub-channel ties one task to the repo:

1. **Open.** Create the sub-channel with `## Owner` (who asked for the work), `## Worker` (the task title, which is `<channel>/<sub-channel>` so the task can be found by title), `## Input`, and `## Output format`. Code work usually takes GitHub URL.
2. **Start.** Start the task with the sub-channel's Input as its text, and record in the sub-channel's `chat.log.jsonl` that it started.
3. **Follow.** Questions and follow-ups go in the sub-channel's conversation and are sent to the task once it is no longer running. Check on it when someone asks or on the next reply run; do not poll.
4. **Collect.** When the task is done, write its summary to the conversation and its main link (usually the pull request) to `output/`. If it failed, record the error and either send a follow-up or start a new task.
5. **Close.** Hub task results disappear when the task is torn down, so tear it down only after step 4. Then set `## Status` to Done and fold the sub-channel into its parent.

The Agents Hub address and token never go in this repository.

**Before opening anything, reuse.** In this order:

1. **Reply in place.** A message goes in the channel it was posted in, even if it fits better elsewhere; answer it and link the better channel.
2. **Extend a channel.** If an existing channel's Input covers the ask, or covers it with a sentence added, add the sentence and keep working there.
3. **Open a sub-channel** only when part of a channel needs a separate output and a separate owner.
4. **Open a channel** only for a new deliverable that no channel's Input covers.

**Keep the list short.**

- **Merge** two channels when they head to the same output: move the conversations and inputs into the older one, regenerate its output, and delete the other.
- **Finish** a channel when its output is delivered and nobody is waiting on it: set `## Status` to `Done`. A message in a Done channel reopens it.
- **Fold** a Done sub-channel back into its parent: move its conversations and inputs up (rename on clashes), put its output into the parent's, and delete the folder.

### How euler replies

euler replies to every new message in a hub chat, in the same conversation, in under 150 words, with three parts in this order:

1. **The answer or result**, in one line.
2. **What changed**, with links (root-relative paths) to the files, output, or sub-channel it touched. Leave this out when nothing changed.
3. **The next step**, or one question, so the conversation keeps going.

When a reply opens, merges, or finishes a channel or sub-channel, it says so in part 2.

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

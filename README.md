# quirq

A small, filesystem-first workspace for quirqy, viewed with [open-chat](https://github.com/sharmasuraj0123/open-chat). This repository contains content, not the Next.js application.

## Five places, five examples

- **Chat** — one folder per person and task, each with a goal, its saved chats, and a generated outcome: Chat/sharmasuraj0123/tasks/getting-started/.
- **Activity** — one feed event: Activity/example.jsonl.
- **Insights** — one insight card: Insights/index.json.
- **Vision** — one short direction document: Vision/example.md.
- **Library** — one website shortcut: Library/example.url.

Each section holds its README plus its content files. The rules for adding, naming, and formatting files are in [CONTRIBUTING.md](CONTRIBUTING.md), and a CI check enforces them on every pull request.

## Open this workspace

Run open-chat locally, click the quirqy name, browse to this directory, and choose **Observe this folder**. If the directory is outside the picker's boundary, set MIRROR_BROWSE_ROOT in the app's .env.local to its parent directory. Alternatively, set MIRROR_ROOT to this directory before starting the app.

Select the root of this repository itself so the links in the examples, which are relative to the root, resolve. The dock in the current open-chat version orders these sections as Chat, Activity, Insights, Vision, Library.

## Change what you see

Edit a file on disk and the active app refreshes automatically. Add JSONL lines to extend the activity feed; change the conversation messages or insight card; edit the vision document; replace the URL with your own address. The app displays these files read-only. The chat example is a saved conversation, without a live model or sample-reply engine. No model, API key, account, or database is required. The Library webpage loads externally; sites that block embedding can be opened with **Open in new tab**.

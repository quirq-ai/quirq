# quirq

This content workspace (quirq/quirq on the hub).

| | |
| --- | --- |
| Repository | [quirq-ai/quirq](https://github.com/quirq-ai/quirq) |
| Visibility | Public |
| Main language | HTML |
| Default branch | `main` |
| Created | 2026-10-27 |
| Last commit | 2026-10-29: agent-channels: open a channel for every agent connected to quirq |

## Purpose

**quirq**: this repository. A small, filesystem-first content workspace for quirqy, read by open-chat and hosted on the hub as `quirq/quirq` on hub.quirq.dev (the source of truth; GitHub mirrors it). It holds five sections: Chat (channels with an input, conversation and output), Activity, Insights, Vision and Library. euler, the hub agent, replies to chats here and keeps the structure in order. This wiki channel lives in it.

## Stack

Content only: Markdown, JSON and JSON Lines, `.url` shortcuts, and HTML outputs. A Python checker enforces the layout in CI; a sync script opens a channel per connected hub agent.

## Structure

| Path | What it holds |
| --- | --- |
| `Chat/<channel>/` | Channels: README (Input, Output format), conversations and hub chat logs, `inputs/`, `output/`, sub-channels |
| `Activity/`, `Insights/`, `Library/`, `Vision/` | The other four sections |
| `CONTRIBUTING.md`, `CLAUDE.md` | The layout contract |
| `.github/scripts/check_structure.py` | The structure checker (with tests) |
| `.github/scripts/sync_agent_channels.py` | Opens `Chat/<agent>/` for each connected agent |

## How to run

```sh
python3 .github/scripts/check_structure.py
git remote add quirq quirq://hub.quirq.dev/quirq/quirq
git pull --no-rebase quirq main && git push quirq main
```

To view it, open the folder in open-chat or browse [hub.quirq.dev/quirq/quirq](https://hub.quirq.dev/quirq/quirq).

## Status

Very active (2026-10-29: agent channels, the tanker mooring simulator and its wiki, and this org wiki).

## Key links

- Code: https://github.com/quirq-ai/quirq
- README: https://github.com/quirq-ai/quirq#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

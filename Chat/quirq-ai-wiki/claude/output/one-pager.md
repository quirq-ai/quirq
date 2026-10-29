# _claude

Archive of the quirq Claude project's conversations (private).

| | |
| --- | --- |
| Repository | [quirq-ai/_claude](https://github.com/quirq-ai/_claude) |
| Visibility | Private |
| Main language | JavaScript |
| Default branch | `main` |
| Created | 2026-10-08 |
| Last commit | 2026-10-29: Daily archive: 6493 messages to 10-29 02:47 UTC |

> Private repo. quirq/quirq is public on GitHub, so this page only says what the repo is for and how it is laid out. Its contents stay in the repo.

## Purpose

The archive of quirq's Claude project: a copy of the project chat and every thread, with authors and times, plus the project's Library and shared folder, with secrets and personal data redacted. It is laid out to be cloned as a `.claude` folder (the underscore is there because cloud sessions cannot attach a repo whose name starts with a dot). Its README says it must stay private.

## Stack

Markdown and JSON Lines, built by Python scripts in `tools/`.

## Structure

| Path | What it holds |
| --- | --- |
| `conversations/` | Project chat and one file per thread, as Markdown and JSONL, plus a cursor |
| `library/` | Files and links attached to messages |
| `project-files/` | Mirrored folders of the project's shared folder |
| `tools/` | Archive, library and mirror builders |

## How to run

```sh
git clone https://github.com/quirq-ai/_claude .claude
```

New messages are added when suraj says "submit claude work" in the project chat; a reviewer checks each submission for secrets.

## Status

Updated daily (last 2026-10-29).

## Key links

- Code: https://github.com/quirq-ai/_claude
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

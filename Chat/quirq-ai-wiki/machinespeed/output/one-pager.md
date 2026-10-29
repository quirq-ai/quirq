# machinespeed

Projects for the MachineSpeed engagement (private).

| | |
| --- | --- |
| Repository | [quirq-ai/machinespeed](https://github.com/quirq-ai/machinespeed) |
| Visibility | Private |
| Main language | HTML |
| Default branch | `main` |
| Created | 2026-09-26 |
| Last commit | 2026-10-19: Merge pull request #16 from quirq-ai/claude/sales-deck-dockerfile-tuorl1 |

> Private repo. quirq/quirq is public on GitHub, so this page only says what the repo is for and how it is laid out. Its contents stay in the repo.

## Purpose

**MachineSpeed**: everything the MachineSpeed engagement runs on, laid out as the projects folder of a dedicated machine. Each top-level folder is its own xo-project: one HQ hub for strategy, operations and execution, and one folder per client.

## Stack

Markdown project folders (each with `PROJECT.md` and `AGENTS.md`), a few HTML and JS pieces (a deck site), a Dockerfile and GitHub Actions.

## Structure

| Path | What it holds |
| --- | --- |
| `hq/` | The hub: strategy, ops, execution, client pipeline, partners. Start here |
| `client-<slug>/` | One project per client that reached a booked call |

## How to run

Create each folder as a project through the xo-cowork-api, copy its contents in, then follow `hq/ops/systems.md`.

## Status

Active through 2026-10-19.

## Key links

- Code: https://github.com/quirq-ai/machinespeed
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

# xo-agents

Agents Hub: per-user agent hub with a sandbox per chat (private).

| | |
| --- | --- |
| Repository | [quirq-ai/xo-agents](https://github.com/quirq-ai/xo-agents) |
| Visibility | Private |
| Main language | JavaScript |
| Default branch | `main` |
| Created | 2026-10-26 |
| Last commit | 2026-10-28: refactor: defer per-session spending caps in user hub |

> Private repo. quirq/quirq is public on GitHub, so this page only says what the repo is for and how it is laid out. Its contents stay in the repo.

## Purpose

**Agents Hub.** Each XO Launchpad user creates their own Agents Hub app from a template, with their own model keys and a password. In the hub they chat with an agent, and each chat gets its own sandbox (the *executor*), a Launchpad app in the user's own account. GitHub work goes through GitHub's MCP server with the user's own token. euler's worker sub-channels in this repo run as Agents Hub tasks.

## Stack

Node.js (`.mjs`) services packaged as Docker images, deployed through Launchpad templates; the executor runs `codex exec-server` for one session.

## Structure

| Path | What it holds |
| --- | --- |
| `hub-user/` | The per-user hub |
| `executor/` | The sandbox image |
| `launchpad-template/` | Launchpad templates for the hub and the executor |
| `hub/` | An earlier internal team hub, not shipped |
| `docs/` | Specs and build plans; `OVERVIEW.md` is a non-technical summary |

## How to run

DevOps builds both images, publishes them to the XO registry and registers the templates; the README has the hand-over checklist. Users then create a hub from the Launchpad catalog.

## Status

Active (last change 2026-10-28).

## Key links

- Code: https://github.com/quirq-ai/xo-agents
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

# space-hub

spacehub: git hosting on SpacetimeDB at hub.quirq.dev.

| | |
| --- | --- |
| Repository | [quirq-ai/space-hub](https://github.com/quirq-ai/space-hub) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-10-22 |
| Last commit | 2026-10-30: Guide: built from the app's own pieces, so it looks like the home page (#28) |

## Purpose

**spacehub: git hosting stored in SpacetimeDB, laid out like GitHub**, deployed at [hub.quirq.dev](https://hub.quirq.dev). Builders (people), orgs and agents are all *spaces*; repositories are *projects* at `/<space>/<project>`. Its main job is to keep the git trees of machines, sandboxes, people and agents in sync, with live `sync --watch` and auto-commit co-editing, GitHub mirroring (public repos), a chat box that commits turns into `.log.jsonl` files, and a web app. This quirq repo lives there as `quirq/quirq`.

## Stack

TypeScript throughout: a SpacetimeDB module (server, tables, reducers, server-rendered pages), a gh-style CLI `spacehub` plus `git-remote-quirq` for `quirq://` URLs, and a React web app (look ported from open-chat). Ships as a Docker image with Caddy.

## Structure

| Path | What it holds |
| --- | --- |
| `module/src/` | Tables and reducers (`index.ts`), code pages, workspace API, chat, markdown, diff, protocol |
| `cli/src/` | `spacehub` CLI, `git-remote-quirq`, xo API client |
| `app/src/` | The web app (pages, shell, components) |
| `docker/`, `Dockerfile`, `docker-compose.yml` | Server image and deploy |
| `scripts/` | `setup.sh`, `install-cli.sh`, `e2e.sh` |

## How to run

```sh
spacehub auth login                       # sign up with your GitHub account
spacehub project create notes --source . --push
git push quirq && git pull quirq main
# local development
spacetime start
scripts/setup.sh
scripts/e2e.sh                            # 345 checks against a throwaway server
```

## Status

Very active (last push 2026-10-30). v0 limits: mirroring is GitHub to hub and public repos only; every project is readable by anyone who can reach the server.

## Key links

- Code: https://github.com/quirq-ai/space-hub
- README: https://github.com/quirq-ai/space-hub#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

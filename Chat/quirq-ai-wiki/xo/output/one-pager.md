# xo

xo, the command line (and server) for the XO Cloud API.

| | |
| --- | --- |
| Repository | [quirq-ai/xo](https://github.com/quirq-ai/xo) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-14 |
| Last commit | 2026-10-27: Hub copies are projects AGENT/NAME, never orgs (#92) |
| Website | https://xo.quirq.dev |

## Purpose

**xo, the command line for the XO Cloud API** (dev.xo.builders). Every endpoint is a command, and xo sends your XO API key without ever printing it. It creates spaces (Codex, Claude Code, OpenClaw kinds), projects and folder spaces on the quirq hub or GitHub, wraps `gh` and shell (`xo gh`, `xo sh`), and also runs as the xo server (`xo serve`) at [xo.quirq.dev](https://xo.quirq.dev).

## Stack

Python 3.11+ standard library only, one argparse command; distributed as `quirq-xo` (PyPI's `xo` is an unrelated game). The server is a WSGI app deployed on Vercel (`app.py`) or Docker. Onboarded to qq. Apache-2.0.

## Structure

| Path | What it holds |
| --- | --- |
| `src/xo/` | CLI, client, commands, server, GitHub and hub (`quirq.py`, `spacerepo.py`) integration, OpenAPI spec |
| `app.py`, `Dockerfile` | Server entry points |
| `docs/` | Quickstart, user guide, Vercel deploy |
| `infra/`, `tests/` | qq manifest and tests |

## How to run

```sh
pip install "quirq-xo @ git+https://github.com/quirq-ai/xo"
xo login
xo status
xo create space my-codex codex --volume-size 20
xo create project notes
xo gh pr list
```

## Status

Very active. Last change 2026-10-27: hub copies are projects `AGENT/NAME`, never orgs.

## Key links

- Code: https://github.com/quirq-ai/xo
- README: https://github.com/quirq-ai/xo#readme
- Live: https://xo.quirq.dev
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

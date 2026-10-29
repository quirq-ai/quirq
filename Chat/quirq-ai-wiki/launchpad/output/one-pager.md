# launchpad

XO Launchpad CLI: create apps and manage deployments.

| | |
| --- | --- |
| Repository | [quirq-ai/launchpad](https://github.com/quirq-ai/launchpad) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-28 |
| Last commit | 2026-10-28: Simplify README and move detailed workflows to user guide |

## Purpose

**XO Launchpad CLI.** Create apps, get Docker commands, and manage deployments on XO Launchpad from the terminal, using the same sign-in as the `xo` CLI. Pushing an image to `registry.xo.builders` deploys the app.

## Stack

Python 3.11+ package `xo-launchpad` (0.2.0) with no runtime dependencies; operations described in `operations.json`. Needs Docker to build and push images. Windows, Linux and macOS.

## Structure

| Path | What it holds |
| --- | --- |
| `src/xo_launchpad/` | CLI and `operations.json` |
| `docs/` | User guide with the detailed workflows |
| `tests/` | Tests |

## How to run

```sh
python -m pip install "xo-launchpad @ git+https://github.com/quirq-ai/launchpad.git"
xo-launchpad auth login            # shares xo's saved login
xo-launchpad app create my-app --port 3000
xo-launchpad app deploy my-app --tag latest --wait
xo-launchpad app status my-app
xo-launchpad app logs my-app
```

## Status

New: created 2026-10-28 and active (README simplified, workflows moved to the user guide).

## Key links

- Code: https://github.com/quirq-ai/launchpad
- README: https://github.com/quirq-ai/launchpad#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

# infra-config

The whole CI/CD system declared as config.

| | |
| --- | --- |
| Repository | [quirq-ai/infra-config](https://github.com/quirq-ai/infra-config) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-21: kinds: add npm-app for npm projects (qq compatibility for every repo) (#38) |

## Purpose

Configuration as code for **quirq infra (qq)**, the CI/CD system for every quirq-ai repo. It declares the whole system as data: which repos are onboarded, what builds them, how a change lands, how releases move through channels, and the limits on what agents may do alone. A change here is a pull request through the same gate as code. Chromium counterpart: `infra/config` plus `lucicfg` (source, then generated output, then an in-sync check). It also holds the qq plan (`docs/plan.md`) and the 51 v0 work items for all thirteen qq repos (`docs/v0.md`).

## Stack

TOML config with JSON Schema, a Python validator and generator (`tools/qqcfg.py`), generated GitHub Actions workflows delivered into product repos, and a drift check that fails when delivered workflows are stale.

## Structure

| Path | What it holds |
| --- | --- |
| `config/*.toml` | The areas: `repos`, `org`, `kinds`, `pipelines`, `gate`, `channels`, `health`, `rollers`, `flakes`, `auto_revert`, `postmortem`, `fuzz`, `perf` |
| `schema/` | JSON Schema per area |
| `generated/github/` | Generated workflows per onboarded repo |
| `templates/` | Workflow templates |
| `tools/qqcfg.py` | validate, generate, get, deliver |
| `docs/plan.md`, `docs/v0.md` | The qq plan and v0 items (suraj's originals) |

Readers: gate, rollers, recipes, sync, test-pipelines, gardener, release and monitoring each read their areas at a pinned commit.

## How to run

```sh
python3 tools/qqcfg.py validate              # the CI check
python3 tools/qqcfg.py validate --todos      # list open decisions
python3 tools/qqcfg.py generate              # rewrite generated/ after editing config/
python3 tools/qqcfg.py deliver xo-space ../xo-space
```

## Status

v0 skeleton built width-first, mostly merged: builders delivered to xo-space, innernet, website and xo. Some of suraj's v0 decisions (canary hour, revert caps, compute ceiling) are decided but not yet written into config.

## Key links

- Code: https://github.com/quirq-ai/infra-config
- README: https://github.com/quirq-ai/infra-config#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

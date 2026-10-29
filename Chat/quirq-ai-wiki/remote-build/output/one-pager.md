# remote-build

Executor interface and action cache.

| | |
| --- | --- |
| Repository | [quirq-ai/remote-build](https://github.com/quirq-ai/remote-build) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-21: infra: qq manifest for the compatibility check (not onboarding) (#9) |

## Purpose

Part of **quirq infra (qq)**. Where actions run and how their results are reused: one executor interface with a `backend` field (`local` and `github` now, `launchpad` and Buildbarn later) and a local action cache keyed by action digest. Actions are shaped like REAPI `Action` and `ActionResult`; every executor verifies the input root digest and platform before running. Chromium counterpart: goma, reclient and Siso with RBE.

## Stack

Python 3.11+ package `qqrbe`, using `qqrecipes` actions by pinned commit; the `github` backend dispatches `.github/workflows/execute.yml`. Apache-2.0.

## Structure

| Path | What it holds |
| --- | --- |
| `src/qqrbe/` | Executor loader, backends, cache, errors, CLI |
| `selftest/` | A small deterministic action used to compare backends |
| `.github/workflows/` | The `execute` worker and CI with the cross-backend job |
| `infra/`, `tests/` | qq manifest and tests |

## How to run

```sh
pip install -e '.[test]'
qqrbe backends
qqrbe selftest --backend local
qqrbe stats
pytest
```

The `github` backend needs a token with `actions: write` (`QQ_GITHUB_TOKEN` or `GITHUB_TOKEN`).

## Status

v0 (V0-RBE-01 and 02) in place. Shared cache is v1, remote execution v2. Last change 2026-10-21.

## Key links

- Code: https://github.com/quirq-ai/remote-build
- README: https://github.com/quirq-ai/remote-build#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

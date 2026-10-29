# gardener

Keeps main green: tree status, bisection, reverts.

| | |
| --- | --- |
| Repository | [quirq-ai/gardener](https://github.com/quirq-ai/gardener) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-21: V0-GAR-01: pin infra-config 40d8f2b, so the gardener watches website and xo (#19) |

## Purpose

Part of **quirq infra (qq)**, quirq-ai's CI/CD system. The gardener keeps `main` green in every onboarded repo: it watches the post-submit run on every main commit, publishes a tree status (open, closed, unknown), groups failures by regression range, bisects them to a culprit, and opens clean reverts within the caps in infra-config's `auto_revert.toml`. Chromium counterpart: sheriff rotations, Sheriff-o-Matic and LUCI Bisection.

## Stack

Python 3.11+ package `qqgarden` (setuptools, jsonschema), reading results through `qqresults` from test-pipelines at a pinned commit. GitHub Actions workflows publish the tree status. Apache-2.0.

## Structure

| Path | What it holds |
| --- | --- |
| `src/qqgarden/` | CLI (`status`, `groups`, `bisect`, revert), GitHub and snapshot backends |
| `pins.toml` | Pinned commits of infra-config and test-pipelines |
| `.github/workflows/` | The `tree-status` workflow and presubmit |
| `tests/` | Offline tests with fixtures |
| `tools/`, `requirements/` | Helpers and locked dependencies |

## How to run

```sh
pip install -e '.[test]'
qqgarden status --config <infra-config checkout>
qqgarden status --config ... --backend snapshot --snapshot tests/fixtures/every-commit.json
qqgarden groups --config <infra-config> --store <results checkout>
pytest
```

## Status

v0 items V0-GAR-01 to 04 merged. Live today: tree status published on the `tree-status` branch for xo-space, innernet, website and xo. Reverts wait on the quirq gardener GitHub App, which does not exist yet, so it reports only.

## Key links

- Code: https://github.com/quirq-ai/gardener
- README: https://github.com/quirq-ai/gardener#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

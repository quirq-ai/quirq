# perf

Performance records per commit.

| | |
| --- | --- |
| Repository | [quirq-ai/perf](https://github.com/quirq-ai/perf) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-21: infra: qq manifest for the compatibility check (not onboarding) (#17) |

## Purpose

Part of **quirq infra (qq)**. Records performance on every post-submit commit of the product repos, so v1 can alert on regressions and v2 can bisect them. v0 only records raw numbers with units and runner type; it does not alert or gate. Chromium counterpart: the chrome.perf waterfall, perf dashboard and Pinpoint.

## Stack

Python 3.11+ package `qqperf`, writing results bundles through `qqresults` (test-pipelines) and building through `qqrecipes`, both by pinned commit. A GitHub Actions workflow runs every 30 minutes. Apache-2.0.

## Structure

| Path | What it holds |
| --- | --- |
| `src/qqperf/` | CLI (record, backlog, manifest) |
| `.github/workflows/perf.yml` | The 30-minute measuring workflow |
| `tools/` | Benchmark scripts |
| `infra/`, `tests/` | qq manifest and tests |

Metrics today: `build-size` (innernet), `xo-space-server-start`, `innernet-search`. Records live on the `perf-data` branch as JSON Lines (`qq-perf-record/1`) and in the test-pipelines store.

## How to run

```sh
pip install -e '.[test,build]'
qqperf --help
pytest
```

## Status

v0 recording live. Last change 2026-10-21.

## Key links

- Code: https://github.com/quirq-ai/perf
- README: https://github.com/quirq-ai/perf#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

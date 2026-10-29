# test-pipelines

Test results, verdicts and failure records.

| | |
| --- | --- |
| Repository | [quirq-ai/test-pipelines](https://github.com/quirq-ai/test-pipelines) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-21: infra: qq manifest for the compatibility check (not onboarding) (#37) |

## Purpose

Part of **quirq infra (qq)**. Turns test output into stored results and mechanical verdicts: write-once **Results** from JUnit XML, **Runs** per gate or post-submit attempt, **Verdicts** (failures retried, then run without the change), **Failure** records per held canary, rollback or auto-revert (mirrored to labelled GitHub issues), and the v0 **scorecard**. Retry policy comes from infra-config's `flakes.toml`. Chromium counterpart: ResultDB and LUCI Analysis.

## Stack

Python 3.11+ package `qqresults` with no runtime dependencies; a composite GitHub Action (`sink/`) that builders add after their test steps. Storage sits behind a `backend` interface. Apache-2.0.

## Structure

| Path | What it holds |
| --- | --- |
| `src/qqresults/` | Store, verdicts, failure records, scorecard, CLI |
| `sink/` | The GitHub Action that stores a job's JUnit results |
| `failure/`, `link/` | Failure-record and linking actions |
| `pins.toml`, `infra/` | Pins and qq manifest |
| `tests/`, `tools/` | Tests with JUnit fixtures and helpers |

## How to run

```yaml
- uses: quirq-ai/test-pipelines/sink@<commit>
  if: always()
  with:
    junit: .qq/out/junit/*.xml
```

```sh
pip install -e '.[test]'
qqresults --help
pytest
```

## Status

v0 in place; used by gardener and perf. Last change 2026-10-21.

## Key links

- Code: https://github.com/quirq-ai/test-pipelines
- README: https://github.com/quirq-ai/test-pipelines#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

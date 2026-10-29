# gate

Required checks and the merge queue.

| | |
| --- | --- |
| Repository | [quirq-ai/gate](https://github.com/quirq-ai/gate) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-09: V0-ORG-03: settings for a user org (--settings, settings check, template) (#32) |

## Purpose

Part of **quirq infra (qq)**. The gate decides what must pass before a change lands: the required checks, computed from infra-config and each repo's manifest, and the merge queue that verifies the exact merge result before it reaches `main`. It is deterministic config, not judgment: no agent can override it. Chromium counterpart: LUCI CV and `commit-queue.cfg`.

## Stack

Python 3.11+ package `qqgate` (jsonschema, PyYAML), reading manifests only through `qqsync` from the sync repo at a pinned commit. Backends per host (`github` now, `launchpad` later). Apache-2.0.

## Structure

| Path | What it holds |
| --- | --- |
| `src/qqgate/` | CLI (`required`, `rule`, `verdict`) and backends |
| `settings/`, `templates/` | Rulesets and merge-queue settings as code |
| `guard/` | The agnosticism guard (no core file names a language or build tool) |
| `timing/` | Gate timing (queue entry to verdict) for the scorecard |
| `pins.toml`, `scripts/`, `docs/`, `tests/` | Pins, the apply script suraj runs, docs, golden tests |

## How to run

```sh
pip install -e '.[test]'
qqgate required --config ../infra-config --repo xo-space
qqgate rule     --config ../infra-config --repo xo-space
qqgate verdict  --config ../infra-config --repo xo-space --sha <commit>
```

Exit codes: 0 pass, 1 refused, 2 undecided, 3 not onboarded.

## Status

v0 in place: xo-space, innernet and website each require their generated `*-presubmit` check. Last change 2026-10-09 (settings for a user org).

## Key links

- Code: https://github.com/quirq-ai/gate
- README: https://github.com/quirq-ai/gate#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

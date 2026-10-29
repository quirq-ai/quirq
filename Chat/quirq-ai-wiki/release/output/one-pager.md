# release

lkgr, channels, canary and rollback.

| | |
| --- | --- |
| Repository | [quirq-ai/release](https://github.com/quirq-ai/release) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-07: docs: README matches release-state today (2026-10-07 docs refresh) (#20) |

## Purpose

Part of **quirq infra (qq)**. Moves builds through **channels**: pointers (`channels/<name>`) that name a commit and artifact digest, moved only by the release executor, which records an operation key before every effect. It computes `lkgr` (newest main commit whose required post-submit builders are all green), cuts and ships a daily `canary` to quirq's research and test environments, and supports promote and rollback. A missing signal means hold, never promote. Chromium counterpart: V8's lkgr finder and LUCI's `promote.py`.

## Stack

Python 3.11+ package `qqrelease`, using `qqgarden` (gardener) and `qqrecipes` by pinned commit; GitHub Actions workflows for lkgr (every 10 minutes) and the canary. It also adds `qq channel` to the qq CLI. Apache-2.0.

## Structure

| Path | What it holds |
| --- | --- |
| `src/qqrelease/` | lkgr, executor, channels, canary and reports |
| `.github/workflows/`, `.github/actions/` | lkgr, canary and presubmit workflows |
| `pins.toml` | Pinned infra-config commit |
| `tools/` | `lkgr_demo.py` and helpers |
| `release-state` branch | `channels.json`, operation records and daily canary reports |

## How to run

```sh
pip install -e '.[test]'
qqrelease lkgr --config <infra-config> --state <state dir> --dry-run
qqrelease channel show --state <state dir>
qqrelease channel rollback --config ... --state ... --repo NAME --channel canary --reason "..." --from COMMIT
pytest
```

## Status

v0 live: canary published since 2026-10-05 for xo-space and innernet. `dev` is off and `stable` is v2. Last change 2026-10-07.

## Key links

- Code: https://github.com/quirq-ai/release
- README: https://github.com/quirq-ai/release#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

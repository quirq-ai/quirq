# qq

The qq command line, version-pinned per repo.

| | |
| --- | --- |
| Repository | [quirq-ai/qq](https://github.com/quirq-ai/qq) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-22: Auto-update qq to qq-setup's reviewed commit, when setup turned it on (#35) |

## Purpose

**qq, the quirq infra command line** (was `quirq-ai/depot` until 2026-10-09). Every repo that qq builds pins its `qq` version in `infra/repo.toml`, and `qq` installs and runs exactly that version, which is how it self-updates. It wraps git and `gh`: fetch and sync pinned dependencies, build and test targets, per-repo commands, and upload and try changes. Chromium counterpart: `depot_tools`.

## Stack

Python 3.11.4+ package `qqdepot` (command `qq`), calling `qqsync` (sync) and `qqrecipes` (recipes) by pinned commit. A `github` backend now, `launchpad` later. Apache-2.0.

## Structure

| Path | What it holds |
| --- | --- |
| `bin/` | The `qq` launcher you put on `PATH` |
| `src/qqdepot/` | CLI and commands |
| `infra/` | qq manifest |
| `tests/` | Tests with fakes and parity adapters |

## How to run

```sh
git clone https://github.com/quirq-ai/qq ~/qq
export PATH="$HOME/qq/bin:$PATH"
qq --version
qq fetch https://github.com/quirq-ai/xo-space   # clone, then qq sync
qq build && qq test
qq upload && qq try
```

Toolchains are published for Linux x86_64 only. Full guide: [docs.quirq.dev/docs/qq](https://docs.quirq.dev/docs/qq).

## Status

Active, version 0.1.0 with no release tag yet. Last change 2026-10-22 (auto-update to setup's reviewed commit).

## Key links

- Code: https://github.com/quirq-ai/qq
- README: https://github.com/quirq-ai/qq#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

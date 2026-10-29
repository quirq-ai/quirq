# sync

The repo manifest schema and its only parser.

| | |
| --- | --- |
| Repository | [quirq-ai/sync](https://github.com/quirq-ai/sync) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-21: infra: qq manifest for the compatibility check (not onboarding) (#17) |

## Purpose

Part of **quirq infra (qq)**. Owns the repo manifest `infra/repo.toml` (schema `quirq-repo/1`): its versioned schema, the only library that reads and edits it (`qqsync`), and the checks that keep pins honest. A manifest lists a repo's pinned qq version, toolchains and dependencies (by sha256 or git commit) and its typed targets. A presubmit guard rejects any other parser. Chromium counterpart: `gclient` and `DEPS`.

## Stack

Python 3.11+ package `qqsync` (jsonschema, tomlkit). Apache-2.0.

## Structure

| Path | What it holds |
| --- | --- |
| `src/qqsync/` | Parser, editor, fetch and verify, `guard`, `project` commands, JSON schema |
| `infra/` | Its own manifest |
| `tests/` | Fixtures and project tests |

## How to run

```sh
pip install -e '.[test]'
qqsync validate infra/repo.toml
qqsync show infra/repo.toml
qqsync pin toolchains python --digest sha256:<64 hex> --version 3.15.0
qqsync fetch toolchains python --dest .qq/python.tar.zst
qqsync verify deps recipes .qq/recipes
```

## Status

Core dependency of qq, recipes, gate, rollers and perf (all pin it by commit). Last change 2026-10-21.

## Key links

- Code: https://github.com/quirq-ai/sync
- README: https://github.com/quirq-ai/sync#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

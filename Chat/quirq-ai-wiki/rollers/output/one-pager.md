# rollers

Rolls pins and lockfiles forward with no human.

| | |
| --- | --- |
| Repository | [quirq-ai/rollers](https://github.com/quirq-ai/rollers) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-21: infra: qq manifest for the compatibility check (not onboarding) (#19) |

## Purpose

Part of **quirq infra (qq)**. Moves pinned dependencies and toolchains forward through the same gate as any other change, with no human in the loop: an agent may land a clean roll alone. Two rollers: toolchain pins in each repo's `infra/repo.toml` (from the digests `toolchains` promoted, edited only through `qqsync`), and lockfiles (Python requirements, `pnpm-lock.yaml`) through Dependabot plus a strict auto-land check. Chromium counterpart: Skia AutoRoll and `roll-dep`.

## Stack

Python 3.11+ package `qqroll`, using `qqsync` by pinned commit; generated Dependabot configs and a `qq-roll-land.yml` workflow per covered repo. Config comes from infra-config's `rollers.toml`. Apache-2.0.

## Structure

| Path | What it holds |
| --- | --- |
| `src/qqroll/` | CLI, toolchain roller, Dependabot generator, `land_check.py` |
| `generated/github/<repo>/` | Generated `dependabot.yml` and `qq-roll-land.yml` per repo |
| `infra-config.commit` | The infra-config commit it reads |
| `infra/`, `tests/`, `requirements/` | qq manifest, tests with fixtures, locked deps |

## How to run

```sh
pip install -e '.[test]'
qqroll --help
qqroll dependabot        # regenerate generated/github/*
pytest
```

## Status

v0 (V0-ROL-01, 02) in place. Last change 2026-10-21.

## Key links

- Code: https://github.com/quirq-ai/rollers
- README: https://github.com/quirq-ai/rollers#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

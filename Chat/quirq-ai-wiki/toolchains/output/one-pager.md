# toolchains

Builds, publishes and promotes pinned toolchains.

| | |
| --- | --- |
| Repository | [quirq-ai/toolchains](https://github.com/quirq-ai/toolchains) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-21: infra: qq manifest for the compatibility check (not onboarding) (#19) |

## Purpose

Part of **quirq infra (qq)**. Builds the toolchains every qq build uses (Node and Python today), publishes them as OCI artifacts on `ghcr.io/quirq-ai/toolchains/<name>` addressed by digest, and promotes them from staging by reviewed pull request into `promoted.toml`, which the rollers read to update pins. Linux x86_64 only. Chromium counterpart: CIPD packages built by 3pp.

## Stack

Shell build scripts per toolchain, a Python tool `tools/qqtc.py` (stage, promote) and `tools/gate.py` (the promotion gate), GitHub Actions and GHCR.

## Structure

| Path | What it holds |
| --- | --- |
| `toolchains/node/`, `toolchains/python/` | `toolchain.toml` (version, source, sha256) and `build.sh` |
| `toolchains.toml` | The toolchain list |
| `promoted.toml` | Promoted digests (node 24.21.0, python 3.14.8); written only by `qqtc promote` |
| `tools/` | `qqtc.py`, `gate.py` |
| `.github/workflows/` | `build` and `promotion-gate` |

## How to run

```sh
# 1. edit toolchains/<name>/toolchain.toml and build.sh, open a PR (CI builds and smoke-tests)
# 2. after landing, CI stages ghcr.io/quirq-ai/toolchains/<name>:staging-...
python tools/qqtc.py promote <name> --record staged.json   # 3. promote in its own PR
```

## Status

v0 in place. The `promotion-gate` check is advisory until gate's settings are next applied. Last change 2026-10-21.

## Key links

- Code: https://github.com/quirq-ai/toolchains
- README: https://github.com/quirq-ai/toolchains#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

# installer

Installs follow a release channel.

| | |
| --- | --- |
| Repository | [quirq-ai/installer](https://github.com/quirq-ai/installer) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-21: infra: qq manifest for the compatibility check (not onboarding) (#11) |

## Purpose

Part of **quirq infra (qq)**. Makes clients follow a release **channel** instead of `main`: it reads which commit and artifact digest each channel names (release's `channels.json` on the `release-state` branch) and can check out and verify an install at exactly that commit. Chromium counterpart: `chrome/updater` (Omaha). In v0 only xo-space test installs in quirq's research and test environments follow `channels/canary`; low priority (P4).

## Stack

Python 3.11+ package `qqinstall` with no runtime dependencies; reads release's manifest (schema `qq-channels/1`). Apache-2.0.

## Structure

| Path | What it holds |
| --- | --- |
| `src/qqinstall/` | CLI: `resolve`, `checkout`, `verify`, `show` |
| `pins.toml` | Pinned release commit (the manifest producer) |
| `infra/` | qq manifest |
| `docs/`, `tests/`, `tools/` | Docs, tests, pin checks |

## How to run

```sh
pip install "qqinstall @ git+https://github.com/quirq-ai/installer@<commit>"
qqinstall resolve  --repo xo-space --channel canary
qqinstall checkout --repo xo-space --channel canary --remote <git URL> --dest ./xo-space
qqinstall verify   --repo xo-space --channel canary --checkout ./xo-space
qqinstall show
```

Exit codes: 0 resolved or verified, 1 mismatch, 2 error, 3 not published.

## Status

V0-INS-01 working: xo-space and innernet canary resolve since the first canary on 2026-10-05. Last change 2026-10-21.

## Key links

- Code: https://github.com/quirq-ai/installer
- README: https://github.com/quirq-ai/installer#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

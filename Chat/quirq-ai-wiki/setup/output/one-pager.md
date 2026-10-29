# setup

One command to install qq and xo and set up an org.

| | |
| --- | --- |
| Repository | [quirq-ai/setup](https://github.com/quirq-ai/setup) |
| Visibility | Public |
| Main language | JavaScript |
| Default branch | `main` |
| Created | 2026-10-06 |
| Last commit | 2026-10-27: Install xo at the xo quickstart's current pin, 82dac60 (#37) |

## Purpose

**qq-setup: one command to install, update or remove qq and xo on your machine, and to set up quirq infra for your GitHub org.** The terminal checks your tools (Node 22+, git, a logged-in `gh`, Python 3.11.4+) and opens one local page in two steps: qq on this machine, then your org's repos. For the org it shows the plan and stops: it creates no repo, opens no PR and changes no setting yet. It only ever acts as your own `gh` login and refuses to run with token env vars set.

## Stack

Node.js CLI with no dependencies, and a Next.js form exported statically to `out/` (committed, checked by `check-form`). ESLint, Playwright e2e with a fake `gh`. Pins of qq and xo in `pins.json`.

## Structure

| Path | What it holds |
| --- | --- |
| `cli/` | The `npx` entry point: checks, install, local server |
| `app/`, `components/`, `lib/` | The setup form |
| `out/` | The committed static build the CLI serves |
| `pins.json` | The qq and xo commits it installs |
| `tests/` | Unit and e2e tests, fake `gh`, fixtures |

## How to run

```sh
npx --allow-remote=root https://codeload.github.com/quirq-ai/setup/tar.gz/<commit>
```

Always pin `<commit>` to the latest commit on `main`. For development: `npm run dev`, `npm test`, `npm run e2e`, `npm run check-form`.

## Status

Active. Last change 2026-10-27 installs xo at the xo quickstart's current pin.

## Key links

- Code: https://github.com/quirq-ai/setup
- README: https://github.com/quirq-ai/setup#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

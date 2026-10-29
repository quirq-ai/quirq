# euler

One local home and dock for Innernet, Quitter and Instants.

| | |
| --- | --- |
| Repository | [quirq-ai/euler](https://github.com/quirq-ai/euler) |
| Visibility | Public |
| Main language | JavaScript |
| Default branch | `main` |
| Created | 2026-09-23 |
| Last commit | 2026-10-19: Pin the apps with qq sync instead of carrying their sources (#2) |

## Purpose

**Euler: your apps, one home, one dock.** A local workspace at `http://localhost:2713` that brings three quirq apps, **Innernet**, **Quitter** and **Instants**, under one Node.js server with a floating dock to switch between them, a Home page with app status and on/off controls, and a customizable blob avatar. Euler keeps only a pinned commit per app plus a small adapter patch that mounts each app under `/app/<name>`; the apps' code stays in their own repos. (Not to be confused with euler, the hub agent that maintains quirq/quirq.)

## Stack

Node.js 24 (`.mjs`), Nx for task orchestration, and qq (`qq fetch`, `qq sync`) to fetch the pinned apps. The bundled apps are Next.js (Innernet, Instants) and Vite (Quitter).

## Structure

| Path | What it holds |
| --- | --- |
| `bin/euler.mjs` | The server and build entry point |
| `app/home` | The Home app (status, controls, avatar editor) |
| `app/adapters/*.patch` | Per-app adapters that mount each app under `/app/<name>` |
| `infra/repo.toml` | qq manifest pinning each app's commit |
| `scripts/` | Setup and app-data migration |
| `docs/`, `tests/` | Deployment docs, images, Node tests |

## How to run

```sh
qq fetch https://github.com/quirq-ai/euler && cd euler
npm ci
npm run setup     # copy pinned apps into app/<name>, apply adapters, install
npm run build
npm start         # http://localhost:2713
```

Needs Node.js 24, Git and qq (Python 3.11.4+). macOS and Linux. Cross-platform checks run in GitHub Actions.

## Status

Active through 2026-10-19 (apps now pinned with `qq sync` instead of vendored).

## Key links

- Code: https://github.com/quirq-ai/euler
- README: https://github.com/quirq-ai/euler#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

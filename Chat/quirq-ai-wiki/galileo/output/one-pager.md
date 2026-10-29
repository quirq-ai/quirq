# galileo

Inspect local apps and files under one bar.

| | |
| --- | --- |
| Repository | [quirq-ai/galileo](https://github.com/quirq-ai/galileo) |
| Visibility | Public |
| Main language | JavaScript |
| Default branch | `main` |
| Created | 2026-09-30 |
| Last commit | 2026-10-01: Make galileo v0: sources, with telescope as its bar and router |

## Purpose

**galileo, the inspector of a space.** It keeps a list of *sources* (an app on a local port, or a folder or file on disk) and shows each one, read only, under one bar called **telescope**. Every source gets its own address, `<name>.localhost:4100`, and telescope follows where you are inside it. galileo starts nothing and only ever reads files; it listens on `127.0.0.1` only.

## Stack

Plain Node.js 20+ ESM with no dependencies; telescope is vanilla JS, HTML and CSS. Tests use `node --test`.

## Structure

| Path | What it holds |
| --- | --- |
| `src/server.mjs`, `src/sources.mjs`, `src/files.mjs`, `src/inject.mjs` | Server, sources API, read-only file serving, bar injection |
| `telescope/` | The bar and router (`telescope.js`, `bridge.js`) |
| `sample-app/` | A sample app to point a source at |
| `demo.mjs` | A scripted demo |
| `docs/`, `test/` | Design notes and tests |

## How to run

```sh
npm start                                            # http://localhost:4100
npm start -- --source web=5173 --source notes=~/notes
npm run demo
npm test
```

## Status

v0, built 2026-09-30 to 2026-10-01; quiet since.

## Key links

- Code: https://github.com/quirq-ai/galileo
- README: https://github.com/quirq-ai/galileo#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

# ui

The quirq UI shadcn registry of Astryx components.

| | |
| --- | --- |
| Repository | [quirq-ai/ui](https://github.com/quirq-ai/ui) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-10-06 |
| Last commit | 2026-10-23: update: rename xo registry to quirq registry |
| Website | https://ui-flame-nine.vercel.app |

## Purpose

**Quirq UI registry**: a shadcn registry plus docs site for every Astryx component, block template and page template, so apps can install them with the shadcn CLI. It serves 166 components, 659 blocks and 55 page templates. Recently renamed from the xo registry to the quirq registry.

## Stack

Next.js and React in TypeScript, Astryx design packages (`@astryxdesign/core`, CLI, neutral theme) with StyleX, Recharts, Heroicons and Lucide. Bun for scripts, Biome for lint and format. Deployed on Vercel.

## Structure

| Path | What it holds |
| --- | --- |
| `registry.json` | The shadcn registry definition |
| `registry/astryx/` | Item sources: components, `blocks/`, `templates/`, `nextjs-setup/` (mostly generated) |
| `scripts/generate-registry.mjs`, `scripts/build-registry.mjs` | Regenerate items from the installed packages; build `public/r/*.json` |
| `src/app/docs/`, `src/app/preview/` | Docs routes and standalone previews |
| `src/docs/`, `src/registry/` | Docs UI and generated catalog |

## How to run

```sh
bun install
bun run dev                 # docs on http://localhost:3000
bun run build
bun run registry:generate   # after bumping @astryxdesign/*
```

Do not hand-edit generated files; add the item to `HAND_WRITTEN` first.

## Status

Active through 2026-10-23.

## Key links

- Code: https://github.com/quirq-ai/ui
- README: https://github.com/quirq-ai/ui#readme
- Live: https://ui-flame-nine.vercel.app
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

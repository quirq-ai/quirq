# wiki

The generated wiki of every public repo's code.

| | |
| --- | --- |
| Repository | [quirq-ai/wiki](https://github.com/quirq-ai/wiki) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-10-01 |
| Last commit | 2026-10-29: [wiki-bot] record repository sizes |
| Website | https://wiki.quirq.dev |

## Purpose

**quirq-ai org wiki** at [wiki.quirq.dev](https://wiki.quirq.dev): a generated map of what lives where across every **public** quirq-ai repo. Each public repo gets a folder, each source directory one Markdown page, plus daily activity and repository-size records. An Astro site renders it as an encyclopedia with full-text search. Private repos are never listed. (This quirq-ai-wiki channel complements it with one human-readable one-pager per repo, private ones included.)

## Stack

A Python generator (`quirq-wiki`, standard library) and an Astro site in TypeScript (remark and rehype, Shiki, Mermaid, Pagefind search), Playwright tests. GitHub Actions keep it in sync. Deployed on Vercel.

## Structure

| Path | What it holds |
| --- | --- |
| `<repo>/` (one per public repo) | Generated pages per source directory |
| `INDEX.md`, `_activity/`, `_sizes/` | Index, activity log, repository sizes |
| `quirq_wiki/` | The generator |
| `src/` | The Astro site |
| `.github/workflows/wiki-sync.yml`, `activity-sync.yml` | Incremental sync on `repository_dispatch`, and daily activity at 06:15 UTC |

## How to run

```sh
npm ci && npm run dev               # the site
npm run build && npm run preview    # with full-text search
pip install -e '.[dev]' && quirq-wiki --help
```

## Status

Very active: the `[wiki-bot]` commits daily (last 2026-10-29, repository sizes).

## Key links

- Code: https://github.com/quirq-ai/wiki
- README: https://github.com/quirq-ai/wiki#readme
- Live: https://wiki.quirq.dev
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

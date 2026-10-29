# quirqy

Explore repositories and their history in interactive 3D.

| | |
| --- | --- |
| Repository | [quirq-ai/quirqy](https://github.com/quirq-ai/quirqy) |
| Visibility | Public |
| Main language | JavaScript |
| Default branch | `quirq` |
| Created | 2026-10-03 |
| Last commit | 2026-10-24: Show repository website beside README in About dock |
| Website | https://quirqy.vercel.app |

## Purpose

**Quirqy: explore repositories, their history and the people around them in interactive 3D.** Built on Observatory's 3D engine and liquid-glass interface, it has three repository apps sharing one selected repo: **Data Lab** (files as atoms and a growth tree, replaying sampled first-parent commit history), **Activity Lab** (pull requests, issues, reviews, comments, forks and contributors) and **About** (README beside the repo's website). Load any public GitHub repo, or the bundled quirq-ai/xo and xo-space examples.

## Stack

Vanilla JavaScript with Three.js, built with Vite; marked, DOMPurify and github-slugger for README rendering. No backend, no token. Deployed on Vercel.

## Structure

| Path | What it holds |
| --- | --- |
| `src/data-lab/`, `src/activity-lab/`, `src/about-lab/` | The three apps |
| `src/scene/`, `src/camera/`, `src/light/`, `src/earth/`, `src/gravity/`, `src/sim/` | Shared 3D engine |
| `src/repository/`, `src/data/` | GitHub import and datasets |
| `src/ui/`, `src/nav/`, `src/branding/` | Glass UI and dock |
| `public/data-lab/`, `public/activity-lab/` | Bundled example datasets |
| `scripts/build-data-examples.mjs` | Refreshes the examples |

## How to run

```sh
git clone --branch quirq https://github.com/quirq-ai/quirqy.git && cd quirqy
npm ci
npm run dev        # http://localhost:5174/data, /activity, /about
npm test
```

Node.js 22.22.2+ or 24.15.0+, and a WebGL browser. Work happens on the `quirq` branch (the default); tags `v0` and `v0.1` mark earlier baselines.

## Status

Active through 2026-10-24 (README and website side by side in the About dock).

## Key links

- Code: https://github.com/quirq-ai/quirqy
- README: https://github.com/quirq-ai/quirqy#readme
- Live: https://quirqy.vercel.app
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

# library

Exact copies of outside GitHub projects, one branch each.

| | |
| --- | --- |
| Repository | [quirq-ai/library](https://github.com/quirq-ai/library) |
| Visibility | Public |
| Main language | JavaScript |
| Default branch | `claude/project-thread-152nwx` |
| Created | 2026-10-21 |
| Last commit | 2026-10-21: Fix the audit's four must-fixes for library #1 |

## Purpose

One repo, one branch per GitHub project: quirq's mirror of outside open-source projects. `main` holds the index and the `library` tool; the `attic` branch keeps retired projects. Each project branch is an exact copy of one upstream commit (same tree id), committed as an orphan with `Upstream-Commit` and `Upstream-Tree` trailers. Big or unlicensed projects become pointer READMEs, copies are scanned for secrets first, and local commits on a project branch survive updates through a three-way merge.

## Stack

A single Node.js 20+ tool (`library`) over git 2.40+, with the index in `library.json`. Apache-2.0 for the tool; each branch keeps its upstream's license.

## Structure

| Path | What it holds |
| --- | --- |
| `library` | The tool: add, get, update, check, retire, index |
| `library.json` | Index, descriptions and limits (50 MB project cap) |
| `infra/` | qq manifest |
| `test/` | Node tests |

## How to run

```sh
git clone --single-branch --depth 1 -b <owner>/<repo> https://github.com/quirq-ai/library.git <repo>   # get one project
git clone --single-branch -b main https://github.com/quirq-ai/library.git && cd library
./library add google-research/timesfm
./library update
./library check --upstream
```

Every writing command takes `--dry-run`. Never clone the whole repo. GitHub Actions should be off for it.

## Status

Active; last change 2026-10-21 fixed the audit's four must-fixes.

## Key links

- Code: https://github.com/quirq-ai/library
- README: https://github.com/quirq-ai/library#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

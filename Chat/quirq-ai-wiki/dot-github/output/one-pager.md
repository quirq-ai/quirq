# .github

The org profile and shared community files.

| | |
| --- | --- |
| Repository | [quirq-ai/.github](https://github.com/quirq-ai/.github) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-08-07 |
| Last commit | 2026-10-21: Profile: quirq as a swarm that learns and grows (#5) |

## Purpose

The organization's public profile and shared community files. GitHub shows `profile/README.md` on [github.com/quirq-ai](https://github.com/quirq-ai), and uses this repo's CONTRIBUTING, SUPPORT, SECURITY, CODE_OF_CONDUCT and issue and pull request templates as defaults for every quirq-ai repo that does not ship its own. The profile pitches quirq as "an autonomous swarm that learns, grows and builds software", running on XO Cloud.

## Stack

Markdown and GitHub configuration, plus one Python validation script (Python 3.12+).

## Structure

| Path | What it holds |
| --- | --- |
| `profile/README.md`, `profile/assets/` | The public org overview and its artwork |
| `CONTRIBUTING.md`, `SUPPORT.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md` | Org-wide community defaults |
| `.github/ISSUE_TEMPLATE/`, `.github/PULL_REQUEST_TEMPLATE.md` | Default issue forms and PR template |
| `.github/workflows/check-content.yml` | CI that runs the validator |
| `docs/maintaining.md` | Profile decisions and the maintenance checklist |
| `scripts/validate.py` | Checks Markdown links, profile assets and GitHub config |

## How to run

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
```

Changes merged to `main` become the live org profile and defaults.

## Status

Active. Last change rewrote the profile around "quirq as a swarm that learns and grows".

## Key links

- Code: https://github.com/quirq-ai/.github
- README: https://github.com/quirq-ai/.github#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

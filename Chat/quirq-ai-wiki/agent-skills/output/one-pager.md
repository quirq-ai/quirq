# agent-skills

Agent skills, starting with explainer-film.

| | |
| --- | --- |
| Repository | [quirq-ai/agent-skills](https://github.com/quirq-ai/agent-skills) |
| Visibility | Public |
| Main language | JavaScript |
| Default branch | `main` |
| Created | 2026-10-06 |
| Last commit | 2026-10-07: explainer-film: note what the quirq-infra example film says that is not live (#4) |

## Purpose

Skills that let an agent do a whole job from one prompt. Each skill is a folder with a `SKILL.md` plus the templates, scripts and references it needs. Today it holds one skill, **explainer-film**: a narrated 1 to 3 minute explainer film (1080p MP4 with captions, a web copy with WebVTT and a poster) for a product, repo or feature, in the engraved-plate style of the Innernet field guide film.

## Stack

Claude Code skills (Markdown), with a Node.js (`.mjs`) film engine, CSS and shell scripts in the skill's `template/`.

## Structure

| Path | What it holds |
| --- | --- |
| `skills/explainer-film/SKILL.md` | What the skill does, when to use it, the steps |
| `skills/explainer-film/template/` | The film engine taken from the Innernet film |
| `skills/explainer-film/references/` | Craft notes and the Innernet reference film's brief, storyboard and script |

## How to run

```sh
git clone https://github.com/quirq-ai/agent-skills
ln -s "$PWD/agent-skills/skills/explainer-film" ~/.claude/skills/explainer-film
```

Then ask Claude Code in plain words, for example "make an explainer film for this repo". Skills that need API keys read them from the environment, never from the repo.

## Status

Active, small (one skill). Apache-2.0.

## Key links

- Code: https://github.com/quirq-ai/agent-skills
- README: https://github.com/quirq-ai/agent-skills#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

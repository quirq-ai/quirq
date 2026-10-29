# experiments

One branch per experiment, with an index.

| | |
| --- | --- |
| Repository | [quirq-ai/experiments](https://github.com/quirq-ai/experiments) |
| Visibility | Public |
| Main language | JavaScript |
| Default branch | `main` |
| Created | 2026-10-15 |
| Last commit | 2026-10-16: Republish named experiments even when nothing changed |

## Purpose

One repo, one branch per experiment. `main` is the index of quirq's experiments (27 at last count, from `rea` and `workbench` to `claude-messages` and `solar-claude`) and holds the tooling that publishes them; the `archive` branch keeps finished ones, one squashed commit each.

## Stack

Shell tooling (`publish`, `archive`, `rename`) and a JSON index. Each experiment branch has its own stack (TypeScript, Electron, Node.js, Vite and Three.js, and so on).

## Structure

| Path | What it holds |
| --- | --- |
| `publish` | Turns each local experiment folder into an orphan branch of the same name, appending a commit per snapshot |
| `archive` | Squashes a finished experiment onto the `archive` branch and deletes its branch |
| `rename` | Moves an experiment's folder, branch and index entry together |
| `experiments.json` | Descriptions, stack labels, `skip` and `owners` lists that drive the README table |
| `.publishignore` | Files never published (dependencies, caches, `.env`, local state) |

## How to run

```sh
git clone --single-branch -b <name> https://github.com/quirq-ai/experiments.git <name>   # get one
./publish               # from a clone of main with experiment folders inside
./publish --dry-run
./archive trees
```

## Status

Active. The README's index table is regenerated on every publish.

## Key links

- Code: https://github.com/quirq-ai/experiments
- README: https://github.com/quirq-ai/experiments#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

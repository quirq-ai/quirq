# recipes

Build adapters per target kind.

| | |
| --- | --- |
| Repository | [quirq-ai/recipes](https://github.com/quirq-ai/recipes) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-10-04 |
| Last commit | 2026-10-21: infra: qq manifest for the compatibility check (not onboarding) (#17) |

## Purpose

Part of **quirq infra (qq)**. Holds one **adapter** per target kind (such as `python-service`, `pytest`, `node-app`), found by one loader. An adapter is the only place in qq that may name a language, build tool or test runner. Each capability (`fetch`, `build`, `test`, `package`, `run`, `deploy`, `bench`, `fuzz`) turns a target into REAPI-shaped actions that run locally, on a GitHub runner, or later on a remote executor. Chromium counterpart: `recipes-py` and the recipes in `tools/build`.

## Stack

Python 3.11+ package `qqrecipes`, using `qqsync` by pinned commit; some adapters ship small Node `.mjs` helpers. Apache-2.0.

## Structure

| Path | What it holds |
| --- | --- |
| `src/qqrecipes/` | Loader, contract (`Adapter`, `Action`), runner, adapters per kind |
| `examples/node-app/`, `examples/python-service/` | Example targets |
| `infra/`, `tests/`, `tools/` | qq manifest, tests with fake adapters, helpers |

## How to run

```sh
pip install -e '.[test]'
qqrecipes --help
qqrecipes check-kinds        # every kind in infra-config has an adapter
pytest
```

## Status

v0 adapters in place and used by perf and release; product CI still runs infra-config's `interim` commands. Last change 2026-10-21.

## Key links

- Code: https://github.com/quirq-ai/recipes
- README: https://github.com/quirq-ai/recipes#readme
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

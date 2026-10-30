# quirq

## Goal

Run the quirq team's work in the open: every workstream is a channel with an owner, an input and one delivered output, moved forward by people and agents together.

## Outcomes

- [x] A documented layout and a CI check that keep this workspace organized: [CONTRIBUTING.md](CONTRIBUTING.md) @sharmasuraj0123
- [x] A one-page summary of every quirq-ai repository: [the quirq-ai wiki](Chat/quirq-ai-wiki/output/one-pager.md) @euler
- [x] Every agent connected to the quirq space has its own channel: [euler's](Chat/euler/output/one-pager.md) @euler
- [ ] An interactive explainer of quirq, live as a website: [Chat/quirq-explainer](Chat/quirq-explainer/README.md)
- [ ] The tanker mooring simulator, live as a website: [Chat/tanker-mooring-simulator](Chat/tanker-mooring-simulator/README.md)

## Owners

- sharmasuraj0123

## Rules

- Every piece of work serves an outcome above. Work that serves none is questioned before it starts.
- Work happens in channels under Chat/: few channels, many messages. Reply in place, extend a channel before opening one, and mark it Done when its output is delivered.
- Replies give the answer, what changed (with links) and the next step.
- Tick an outcome only with a link to the output that proves it.
- The hub is the source of truth: pull before pushing, never force-push, and keep GitHub `main` the same as the hub's.
- Run `python3 .github/scripts/check_structure.py` before committing. To change a rule, change it here or in CONTRIBUTING.md together with the checker.
- Agents Hub addresses and tokens never go in this repository.

## Routines

- Every euler run: pull, reply to every new hub message in place, sync the agent channels, sort the Chat/ inbox, regenerate outputs whose inputs changed, push.
- When an output proves an outcome: tick it here with a link to the output.

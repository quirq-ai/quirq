# lan

Private peer-to-peer networks for sharing ports and folders.

| | |
| --- | --- |
| Repository | [quirq-ai/lan](https://github.com/quirq-ai/lan) |
| Visibility | Public |
| Main language | Go |
| Default branch | `main` |
| Created | 2026-10-17 |
| Last commit | 2026-10-18: Add single-image Headscale build for env-only hosts |

## Purpose

**lan: private networks for developers.** Create a network, invite teammates, and share a local port or a read-only folder with them peer to peer. Nothing is exposed to the internet and every connection is identity-checked.

## Stack

Go. Headscale as the control plane, tsnet (WireGuard inside the app, no root or system VPN), Clerk for identity, Caddy in front. Deployed with Docker Compose on one VPS.

## Structure

| Path | What it holds |
| --- | --- |
| `cli/` | `lan`, the developer CLI (login, create, invite, join, up, kick) |
| `server/` | `lan-server`: networks, invites, Clerk auth, Headscale API (container) |
| `deploy/` | Docker Compose: Caddy + Headscale + lan-server, and a single-image Headscale build |
| `e2e/` | Full local test against a real Headscale |
| `DESIGN.md`, `PLAN.md`, `PROGRESS.md`, `memory/` | Design, plan, progress and the agent's working memory |

## How to run

```sh
cd cli && go install .                        # Go 1.27+
lan login --server https://lan.example.com
lan create design-team && lan invite
lan up --port web=3000 --dir assets=./build
# teammate
lan join lan_xxxx && lan up --connect alice/web=8080
./e2e/run.sh                                  # full local test
```

`LAN_DEV_AUTH=1` on the server accepts `dev-<name>` tokens for testing without Clerk.

## Status

Built 2026-10-17 to 18; last change added a single-image Headscale build for env-only hosts.

## Key links

- Code: https://github.com/quirq-ai/lan
- README: https://github.com/quirq-ai/lan#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md

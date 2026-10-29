#!/usr/bin/env python3
"""Give every agent connected to the quirq space its own channel, Chat/<agent>/.

Run it from the root of a clone of quirq/quirq that is up to date with the
hub's main. It asks the hub which agents are connected to the space
(`spacehub agent list`), then for each one:

- opens Chat/<agent>/ if it is missing: README.md with "## Agent", chat.json,
  and chat.log.jsonl, so the hub shows a chat for it;
- appends a status turn to chat.log.jsonl when where it is connected or
  running changes, and an activity turn listing its new commits here;
- rewrites output/one-pager.md, the agent's profile and recent activity;
- sets "## Status" to Done when the agent is no longer connected, and back to
  Open when it returns.

It only writes files; the caller commits and pushes them to the hub. Its own
commits use the subject prefix "agent-channels:", which it leaves out of the
activity it reports. --agents <file> reads `spacehub agent list` output from a
file instead of asking the hub (for tests).
"""

import argparse
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

SPACE = "quirq"
HUB = "https://hub.quirq.dev"
COMMIT_PREFIX = "agent-channels:"
# Turns this script writes are authored by euler, the agent that runs it.
WRITER = "euler"
FIRST_ACTIVITY = 5
MAX_LISTED = 10
AGENT_LINE_RE = re.compile(
    r"^(?P<name>[a-z0-9][a-z0-9-]*)\s+owned by (?P<owner>\S+)\s+"
    r"connected to (?P<connected>.+?)\s+(?:running on (?P<hosts>.+)|not running)$"
)
STATUS_RE = re.compile(r"^(## Status\n+)(\S+)", re.MULTILINE)


def run(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def parse_agents(listing):
    agents = {}
    for line in listing.splitlines():
        match = AGENT_LINE_RE.match(line.strip())
        if not match:
            continue
        connected = match["connected"]
        agents[match["name"]] = {
            "owner": match["owner"],
            "connected": [] if connected == "nothing" else connected.split(", "),
            "hosts": match["hosts"].split(", ") if match["hosts"] else [],
        }
    return agents


def description(name, offline):
    if offline:
        return ""
    try:
        lines = run("spacehub", "agent", "view", name).splitlines()
    except (OSError, subprocess.CalledProcessError):
        return ""
    # `agent view` prints the name, then the description, then a blank line.
    return lines[1].strip() if len(lines) > 1 and lines[1].strip() else ""


def commits(name, since=None, limit=None):
    """The agent's own commits on HEAD, newest first, without this script's."""
    args = ["git", "log", "--no-merges", f"--author=^{name} <", "--format=%H%x09%cI%x09%s"]
    if limit:
        # Extra room for this script's commits, which are filtered out below.
        args.append(f"-{limit * 4}")
    if since:
        args.append(f"{since}..HEAD")
    found = []
    for line in run(*args).splitlines():
        sha, time, subject = line.split("\t", 2)
        if not subject.startswith(COMMIT_PREFIX):
            found.append({"sha": sha, "time": time, "subject": subject})
    return found[:limit] if limit else found


def touched_files(shas):
    files = []
    for sha in shas:
        for path in run("git", "show", "--format=", "--name-only", sha).splitlines():
            if path and path not in files and Path(path).is_file():
                files.append(path)
    return files[:MAX_LISTED]


def read_log(path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def status_text(name, agent):
    if SPACE not in agent["connected"]:
        return f"{name} is no longer connected to {SPACE}."
    running = f"running on {', '.join(agent['hosts'])}" if agent["hosts"] else "not running"
    return f"{name} is connected to {', '.join(agent['connected'])} and {running}."


def listed(found):
    lines = [f"- {c['subject']} ({c['sha'][:7]})" for c in found[:MAX_LISTED]]
    if len(found) > MAX_LISTED:
        lines.append(f"- and {len(found) - MAX_LISTED} more")
    return "\n".join(lines)


def write(path, text):
    """Write text if it changed; return whether it did."""
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def open_channel(folder, name, about):
    write(
        folder / "README.md",
        f"# {name}\n\n"
        f"## Input\n\n{name}'s channel, opened when {name} connected to the {SPACE} space. "
        f"Talk to {name} here: its status and the work it pushes show up in this chat. "
        "Drop files for it in inputs/.\n\n"
        f"## Output format\n\nOne pager\n\n## Agent\n\n{name}\n\n## Status\n\nOpen\n",
    )
    write(
        folder / "chat.json",
        json.dumps(
            {
                "type": "conversation",
                "title": f"{name}'s channel",
                "subtitle": about or f"An agent connected to {SPACE}.",
                "messages": [
                    {
                        "role": "assistant",
                        "content": f"This is {name}'s channel. Its status and activity in {SPACE} appear here, and you can talk to it below.",
                    }
                ],
            },
            indent=2,
        )
        + "\n",
    )


def set_status(readme, value):
    text = readme.read_text(encoding="utf-8")
    if STATUS_RE.search(text):
        text = STATUS_RE.sub(lambda m: m[1] + value, text, count=1)
    else:
        text = text.rstrip("\n") + f"\n\n## Status\n\n{value}\n"
    write(readme, text)


def one_pager(name, agent, about, recent):
    connected = ", ".join(agent["connected"]) or "nothing"
    running = ", ".join(agent["hosts"]) or "not running"
    text = f"# {name}\n\n"
    if about:
        text += f"{about}\n\n"
    text += (
        f"- Owned by: {agent['owner']}\n"
        f"- Connected to: {connected}\n"
        f"- Running on: {running}\n"
        f"- Definition: [{name}/home]({HUB}/{name}/home)\n\n"
        "## Recent activity in quirq\n\n"
    )
    text += (listed(recent) if recent else "No commits yet.") + "\n"
    return text


def sync_agent(name, agent, offline):
    folder = Path("Chat") / name
    readme, log = folder / "README.md", folder / "chat.log.jsonl"
    connected = SPACE in agent["connected"]
    if folder.exists() and "## Agent" not in (readme.read_text(encoding="utf-8") if readme.exists() else ""):
        print(f"skip {name}: Chat/{name}/ is a channel that is not {name}'s")
        return
    if not folder.exists():
        if not connected:
            return
        open_channel(folder, name, description(name, offline))
        print(f"opened Chat/{name}/")
    about = description(name, offline)
    turns = read_log(log)
    new = []

    status = status_text(name, agent)
    last_status = next((t["content"] for t in reversed(turns) if str(t.get("id", "")).startswith("status-")), None)
    if status != last_status:
        new.append({"id": f"status-{now().replace(':', '').replace('.', '')[:17]}", "role": "assistant",
                    "author": WRITER, "content": status, "time": now()})
    set_status(readme, "Open" if connected else "Done")

    cursor = next((t["id"][len("activity-"):] for t in reversed(turns) if str(t.get("id", "")).startswith("activity-")), None)
    try:
        found = commits(name, since=cursor) if cursor else commits(name, limit=FIRST_ACTIVITY)
    except subprocess.CalledProcessError:
        found = commits(name, limit=FIRST_ACTIVITY)  # the cursor left history
    if found:
        heading = (f"{name}'s latest work in {SPACE}/{SPACE}" if not cursor
                   else f"{name} pushed {len(found)} commit{'s' if len(found) > 1 else ''} to {SPACE}/{SPACE}")
        turn = {"id": f"activity-{found[0]['sha']}", "role": "assistant", "author": WRITER,
                "content": f"{heading}:\n{listed(found)}", "time": found[0]["time"]}
        files = touched_files([c["sha"] for c in found])
        if files:
            turn["links"] = [{"label": path, "path": path} for path in files]
        new.append(turn)

    if new:
        with log.open("a", encoding="utf-8") as out:
            for turn in new:
                out.write(json.dumps(turn, ensure_ascii=False, separators=(",", ":")) + "\n")
        print(f"Chat/{name}/chat.log.jsonl: {len(new)} new turn(s)")
    write(folder / "output/one-pager.md", one_pager(name, agent, about, commits(name, limit=MAX_LISTED)))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--agents", help="read `spacehub agent list` output from this file")
    args = parser.parse_args()
    listing = Path(args.agents).read_text(encoding="utf-8") if args.agents else run("spacehub", "agent", "list", SPACE)
    agents = parse_agents(listing)
    # Agents that left keep their channel; it is marked Done.
    for folder in sorted(Path("Chat").iterdir()):
        readme = folder / "README.md"
        if folder.name not in agents and readme.is_file() and "## Agent" in readme.read_text(encoding="utf-8"):
            agents[folder.name] = {"owner": "unknown", "connected": [], "hosts": []}
    for name in sorted(agents):
        sync_agent(name, agents[name], offline=bool(args.agents))


if __name__ == "__main__":
    sys.exit(main())

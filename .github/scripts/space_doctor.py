#!/usr/bin/env python3
"""List the upkeep the quirq workspace is owed right now.

check_structure.py says whether the repo is valid; this says what euler
should do on its next run (see "Running itself" in CONTRIBUTING.md). It
prints one task per line as "<kind>\t<path>\t<reason>", or "Nothing to do.",
and always exits 0. Pass --json for a JSON list instead.

Times come from git commit dates and the chat logs' "time" fields, so run it
on a checkout that is up to date with the hub.
"""

import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_structure import (  # noqa: E402
    CHAT_LOG_SUFFIX,
    OUTPUT_FORMATS,
    ROOT,
    markdown_sections,
    split_channel,
    tracked_files,
)

# An Open channel with no commit for this long is finished.
STALE_SECONDS = 14 * 24 * 3600
# A Waiting question unanswered for this long takes its recommended default.
WAITING_SECONDS = 48 * 3600
# Run order: replies first, so people are never kept waiting by upkeep.
KINDS = ("reply", "sort-inbox", "fold", "regenerate", "missing-output", "default", "stale")


def commit_time(*paths):
    """Unix time of the newest commit touching any of paths, or 0."""
    out = subprocess.run(
        ["git", "log", "-1", "--format=%ct", "--", *map(str, paths)],
        cwd=ROOT, check=True, capture_output=True, text=True,
    ).stdout.strip()
    return int(out) if out else 0


def turn_time(turn):
    try:
        return datetime.fromisoformat(str(turn["time"]).replace("Z", "+00:00")).timestamp()
    except (KeyError, ValueError):
        return 0


def last_turn(path):
    """The last turn of a chat log or conversation, or None."""
    text = (ROOT / path).read_text(encoding="utf-8")
    try:
        if path.name.endswith(CHAT_LOG_SUFFIX):
            lines = [l for l in text.splitlines() if l.strip()]
            return json.loads(lines[-1]) if lines else None
        messages = json.loads(text).get("messages") or []
        return messages[-1] if messages else None
    except (json.JSONDecodeError, AttributeError):
        return None  # the checker reports broken files


def channels(files):
    """Map each channel folder to its README sections and its files."""
    found = {}
    for path in files:
        split = split_channel(path) if path.parts[0] == "Chat" else None
        if split is None:
            continue
        channel_dir, rest = split
        channel = found.setdefault(channel_dir, {"sections": None, "files": []})
        channel["files"].append((path, rest))
        if rest == ("README.md",):
            channel["sections"] = markdown_sections((ROOT / path).read_text(encoding="utf-8"))
    return {d: c for d, c in found.items() if c["sections"] is not None}


def first(sections, name, default=""):
    lines = sections.get(name) or []
    return lines[0].lower() if lines else default


def tasks(now):
    files = tracked_files()
    found = []

    def add(kind, path, reason):
        found.append({"kind": kind, "path": str(path), "reason": reason})

    for path in files:
        if path.parts[0] == "Chat" and len(path.parts) == 2 and path.name != "README.md":
            add("sort-inbox", path, "file waiting in the Chat/ inbox")

    for channel_dir, channel in sorted(channels(files).items()):
        sections = channel["sections"]
        status = first(sections, "Status", "open")
        is_sub = len(channel_dir.parts) > 2
        is_agent = "Agent" in sections
        own = [(p, r) for p, r in channel["files"] if len(r) == 1 or r[0] == "inputs"]

        logs = {p for p, r in own if p.name.endswith(CHAT_LOG_SUFFIX)}
        for path, rest in own:
            if len(rest) != 1 or path.name == "README.md":
                continue
            if not path.name.endswith(CHAT_LOG_SUFFIX):
                # A conversation with a log gets its new turns in the log.
                if path.with_name(path.stem + CHAT_LOG_SUFFIX) in logs:
                    continue
            turn = last_turn(path)
            if turn and turn.get("role") == "user":
                add("reply", path, "last turn is from " + str(turn.get("author") or "a user"))

        if is_sub and status == "done":
            add("fold", channel_dir, "sub-channel is Done; fold it into " + str(channel_dir.parent))
            continue
        if status == "done" or is_agent:
            continue  # agent channels are kept by sync_agent_channels.py

        last_activity = commit_time(channel_dir)
        if status == "waiting":
            if now - last_activity > WAITING_SECONDS:
                add("default", channel_dir, "Waiting for over 48 hours; apply the recommended default")
            continue

        output_format = first(sections, "Output format")
        if output_format in OUTPUT_FORMATS:
            output = channel_dir / "output" / OUTPUT_FORMATS[output_format]
            if output not in files:
                add("missing-output", output, "channel has no output yet")
            else:
                # Chat turns are acted on in the reply; only new inputs are
                # owed a regeneration on their own.
                if commit_time(channel_dir / "inputs") > commit_time(output):
                    add("regenerate", output, "inputs/ changed after the output")

        personal = first(sections, "Owner") == channel_dir.name
        if not is_sub and not personal and now - last_activity > STALE_SECONDS:
            add("stale", channel_dir, "no commit for 14 days; set Status to Done")

    return sorted(found, key=lambda t: (KINDS.index(t["kind"]), t["path"]))


def main():
    found = tasks(time.time())
    if "--json" in sys.argv[1:]:
        print(json.dumps(found, indent=2))
    elif not found:
        print("Nothing to do.")
    else:
        for t in found:
            print(f"{t['kind']}\t{t['path']}\t{t['reason']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

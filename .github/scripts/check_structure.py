#!/usr/bin/env python3
"""Check that the quirq workspace follows the rules in CONTRIBUTING.md.

Runs on tracked files only (git ls-files), uses the standard library only,
and exits non-zero with one line per problem.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Each section and the one content extension it accepts.
SECTIONS = {
    "Activity": ".jsonl",
    "Chat": ".json",
    "Insights": ".json",
    "Library": ".url",
    "Vision": ".md",
}

ROOT_FILES = {
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CLAUDE.md",
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
}
ROOT_DIRS = {".github"} | set(SECTIONS)

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.[a-z]+$")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# Chat is the one nested section: each channel is Chat/<channel>/ and holds
# README.md, conversations (*.json and their *.log.jsonl), inputs/,
# output/<file for the output format>, and sub-channels: worker threads that
# a person or an agent opens as Chat/<channel>/<sub-channel>/, with the same
# shape. Sub-channels go one level deep.
CHANNEL_PARTS = {"inputs", "output"}
MAX_CHANNEL_LEVELS = 2
# "## Status" in a channel README, when present.
CHANNEL_STATUSES = {"open", "done"}
# Files dropped straight into Chat/ wait there until Claude sorts them into
# channels. They and a channel's inputs/ may be any type, so they skip the
# text checks and only have a larger size limit.
MAX_FREE_FORM_BYTES = 25_000_000
# Output format (first line of "## Output format", any case) -> output file.
OUTPUT_FORMATS = {
    "slides": "slides.md",
    "one pager": "one-pager.md",
    "website": "index.html",
    "github url": "github.url",
}
FORMAT_NAMES = "Slides, One pager, Website, GitHub URL"
GITHUB_URL_RE = re.compile(r"^https://github\.com/\S+$")
SLIDE_BREAK_RE = re.compile(r"^---[ \t]*$", re.MULTILINE)
URL_RE = re.compile(r"^https?://\S+$")
# Paths that only exist on one person's machine.
LOCAL_PATH_RE = re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/]|/Users/|/home/|\\\\")
MAX_BYTES = 1_000_000

ACTIVITY_KEYS = ("author", "type", "title", "content")
CHAT_ROLES = {"user", "assistant"}
# The hub's chat box (hub.quirq.dev) appends new turns to
# <name>.log.jsonl beside <name>.json, one JSON object per line.
CHAT_LOG_SUFFIX = ".log.jsonl"

errors = []


def fail(path, message):
    errors.append(f"{path}: {message}")


def tracked_files():
    out = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
    ).stdout
    return [Path(p) for p in out.decode().split("\0") if p]


def check_link(path, target):
    if not isinstance(target, str) or not (ROOT / target).is_file():
        fail(path, f"link path {target!r} does not point to a file in the repo")


def check_text(path, raw):
    if len(raw) > MAX_BYTES:
        fail(path, f"larger than {MAX_BYTES} bytes")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        fail(path, "not valid UTF-8")
        return None
    if text.startswith("﻿"):
        fail(path, "starts with a byte order mark")
    if "\r" in text:
        fail(path, "uses CRLF line endings; use LF")
    if text and not text.endswith("\n"):
        fail(path, "missing final newline")
    if not text.strip():
        fail(path, "is empty")
    if path.parts[0] != ".github" and LOCAL_PATH_RE.search(text):
        fail(path, "contains a machine-specific path; use a path relative to the repo root")
    return text


def check_chat(path, data):
    if data.get("type") != "conversation":
        fail(path, 'type must be "conversation"')
    if not isinstance(data.get("title"), str):
        fail(path, "title must be a string")
    messages = data.get("messages")
    if not isinstance(messages, list) or not messages:
        fail(path, "messages must be a non-empty list")
        return
    for i, msg in enumerate(messages):
        if not isinstance(msg, dict):
            fail(path, f"messages[{i}] must be an object")
            continue
        if msg.get("role") not in CHAT_ROLES:
            fail(path, f"messages[{i}].role must be one of {sorted(CHAT_ROLES)}")
        if not isinstance(msg.get("content"), str):
            fail(path, f"messages[{i}].content must be a string")
        for link in msg.get("links", []):
            check_link(path, link.get("path") if isinstance(link, dict) else None)


def check_chat_log(path, text):
    stem = path.name[: -len(CHAT_LOG_SUFFIX)]
    if not SLUG_RE.match(stem):
        fail(path, "file names are lowercase kebab-case, e.g. kickoff.log.jsonl")
        return
    if not (ROOT / path.parent / f"{stem}.json").is_file():
        fail(path, f"a chat log sits beside its conversation; {stem}.json is missing")
    turns = 0
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            turn = json.loads(line)
        except json.JSONDecodeError as e:
            fail(path, f"line {n} is not valid JSON ({e.msg})")
            continue
        turns += 1
        if not isinstance(turn, dict):
            fail(path, f"line {n} must be a JSON object")
            continue
        if turn.get("role") not in CHAT_ROLES:
            fail(path, f"line {n} role must be one of {sorted(CHAT_ROLES)}")
        if not isinstance(turn.get("content"), str):
            fail(path, f"line {n} needs a string 'content'")
        for link in turn.get("links", []):
            check_link(path, link.get("path") if isinstance(link, dict) else None)
    if not turns:
        fail(path, "has no turns")


def check_insights(path, data):
    if data.get("type") != "collection":
        fail(path, 'type must be "collection"')
    if not isinstance(data.get("title"), str):
        fail(path, "title must be a string")
    items = data.get("items")
    if not isinstance(items, list) or not items:
        fail(path, "items must be a non-empty list")
        return
    for i, item in enumerate(items):
        if not isinstance(item, dict) or not isinstance(item.get("title"), str):
            fail(path, f"items[{i}] must be an object with a string title")
            continue
        if "path" in item:
            check_link(path, item["path"])


def check_activity(path, text):
    records = 0
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as e:
            fail(path, f"line {n} is not valid JSON ({e.msg})")
            continue
        records += 1
        if not isinstance(record, dict):
            fail(path, f"line {n} must be a JSON object")
            continue
        for key in ACTIVITY_KEYS:
            if not isinstance(record.get(key), str):
                fail(path, f"line {n} needs a string {key!r}")
    if not records:
        fail(path, "has no records")


def check_library(path, text):
    lines = [l for l in text.splitlines() if l.strip()]
    if len(lines) != 1 or not URL_RE.match(lines[0]):
        fail(path, "must contain exactly one http(s) URL")


def check_markdown(path, text):
    if not text.startswith("# "):
        fail(path, 'must start with a level-1 heading ("# Title")')


def markdown_sections(text):
    """Map each "## Heading" to the non-blank lines under it."""
    sections, current = {}, None
    for line in text.splitlines():
        if line.startswith("## "):
            current = sections.setdefault(line[3:].strip(), [])
        elif line.startswith("#"):
            current = None
        elif current is not None and line.strip():
            current.append(line.strip())
    return sections


def check_channel_readme(path, text, is_sub):
    """Check a channel README and return its output format, or None."""
    check_markdown(path, text)
    sections = markdown_sections(text)
    if is_sub and not sections.get("Owner"):
        fail(path, 'sub-channel README needs an "## Owner" section: the GitHub login or agent that opened it')
    agent = sections.get("Agent")
    if agent is not None and (is_sub or agent[:1] != [path.parent.name]):
        fail(path, '"## Agent" marks an agent\'s own channel: a top-level channel named after the agent, with that name under it')
    if "Worker" in sections and not sections["Worker"]:
        fail(path, '"## Worker" needs text: the Agents Hub task title that runs this sub-channel')
    status = sections.get("Status")
    if status is not None and (not status or status[0].lower() not in CHANNEL_STATUSES):
        fail(path, '"## Status" must be Open or Done')
    if not sections.get("Input"):
        fail(path, 'channel README needs an "## Input" section with text under it')
    output = sections.get("Output format")
    if not output:
        fail(path, f'channel README needs an "## Output format" section: one of {FORMAT_NAMES}')
        return None
    if output[0].lower() not in OUTPUT_FORMATS:
        fail(path, f"output format {output[0]!r} is not one of {FORMAT_NAMES}")
        return None
    return output[0].lower()


def split_channel(path):
    """Split a path under Chat/ into (channel folder, path inside it).

    Returns None for Chat/README.md and inbox files directly in Chat/.
    """
    parts = path.parts
    if len(parts) <= 2:
        return None
    level = 2
    while (
        len(parts) > level + 1
        and parts[level] not in CHANNEL_PARTS
        and level - 1 < MAX_CHANNEL_LEVELS
    ):
        level += 1
    return Path(*parts[:level]), parts[level:]


def check_channel_names(path, channel_dir):
    for name in channel_dir.parts[1:]:
        if not SLUG_RE.match(name):
            fail(path, f"channel {name!r} must be lowercase kebab-case")
            return False
    return True


def check_free_form(path, inbox):
    """Check an inbox file or a channel input; return False if path is neither."""
    split = split_channel(path)
    is_inbox = split is None and path.name != "README.md"
    is_input = split is not None and len(split[1]) == 2 and split[1][0] == "inputs"
    if not (is_inbox or is_input):
        return False
    if (ROOT / path).stat().st_size > MAX_FREE_FORM_BYTES:
        fail(path, f"larger than {MAX_FREE_FORM_BYTES} bytes")
    if is_inbox:
        inbox.append(path)
    elif not check_channel_names(path, split[0]):
        pass
    elif not NAME_RE.match(path.name):
        fail(path, "input files are lowercase kebab-case, e.g. pricing-notes.pdf")
    return True


def check_chat_layout(path, text, channels):
    """Check one file under Chat/ against the channel layout.

    Returns True when the file is a conversation that still needs its
    content checked. Output files are collected in channels and checked
    once the channel's output format is known.
    """
    split = split_channel(path)
    if split is None:
        check_markdown(path, text)
        return False
    channel_dir, rest = split
    if not check_channel_names(path, channel_dir):
        return False
    channel = channels.setdefault(channel_dir, {"readme": False, "format": None, "output": []})
    if len(rest) == 1:
        if path.name == "README.md":
            channel["readme"] = True
            channel["format"] = check_channel_readme(path, text, len(channel_dir.parts) > 2)
            return False
        if path.name.endswith(CHAT_LOG_SUFFIX):
            check_chat_log(path, text)
            return False
        return True
    if len(rest) == 2 and rest[0] == "output":
        channel["output"].append((path, text))
        return False
    fail(path, "a channel holds only README.md, conversations, inputs/, output/, and sub-channels one level deep")
    return False


def check_output(path, text, output_format):
    expected = OUTPUT_FORMATS[output_format]
    if path.name != expected:
        fail(path, f"the output for this channel's output format is output/{expected}")
    elif expected == "github.url":
        lines = [l for l in text.splitlines() if l.strip()]
        if len(lines) != 1 or not GITHUB_URL_RE.match(lines[0]):
            fail(path, "must contain exactly one https://github.com/ URL")
    elif expected == "index.html":
        if "<html" not in text.lower():
            fail(path, "must be a complete HTML page")
    else:
        check_markdown(path, text)
        if expected == "slides.md" and not SLIDE_BREAK_RE.search(text):
            fail(path, 'slides are separated by a line containing only "---"')


def check_channels(channels):
    for channel_dir, channel in sorted(channels.items()):
        if not channel["readme"]:
            fail(channel_dir, "channel is missing its README.md")
        if len(channel_dir.parts) > 2 and channel_dir.parent not in channels:
            fail(channel_dir, "sub-channel's parent channel has no README.md")
        if channel["format"] is None:
            continue
        for path, text in channel["output"]:
            check_output(path, text, channel["format"])


def check_content(path, text):
    section = path.parts[0]
    if section == "Activity":
        check_activity(path, text)
    elif section == "Library":
        check_library(path, text)
    elif section == "Vision":
        check_markdown(path, text)
    else:
        try:
            data = json.loads(text)
        except json.JSONDecodeError as e:
            fail(path, f"not valid JSON ({e.msg} at line {e.lineno})")
            return
        if not isinstance(data, dict):
            fail(path, "must be a JSON object")
        elif section == "Chat":
            check_chat(path, data)
        else:
            check_insights(path, data)


def main():
    files = tracked_files()
    seen_sections = set()
    chat_channels = {}
    inbox = []

    for path in files:
        top = path.parts[0]
        if len(path.parts) == 1:
            if top not in ROOT_FILES:
                fail(path, "not an allowed top-level file (see CONTRIBUTING.md)")
        elif top not in ROOT_DIRS:
            fail(path, "not inside an allowed top-level folder (see CONTRIBUTING.md)")

        if top == "Chat" and check_free_form(path, inbox):
            seen_sections.add(top)
            continue

        text = check_text(path, (ROOT / path).read_bytes())
        if text is None or top not in SECTIONS:
            if path.name.endswith(".md") and text is not None:
                check_markdown(path, text)
            continue

        seen_sections.add(top)
        if top == "Chat":
            if not check_chat_layout(path, text, chat_channels):
                continue
        elif len(path.parts) != 2:
            fail(path, "sections are flat; no subfolders")
            continue
        if path.name == "README.md":
            check_markdown(path, text)
            continue
        if path.suffix != SECTIONS[top]:
            fail(path, f"{top}/ only holds {SECTIONS[top]} files")
            continue
        if not NAME_RE.match(path.name):
            fail(path, "file names are lowercase kebab-case, e.g. weekly-review" + SECTIONS[top])
            continue
        check_content(path, text)

    check_channels(chat_channels)

    for section in SECTIONS:
        if section not in seen_sections or not (ROOT / section / "README.md").is_file():
            fail(Path(section), "section is missing its README.md")

    if inbox:
        print(f"Note: {len(inbox)} unsorted file(s) waiting in Chat/ to be sorted into channels:")
        for path in inbox:
            print(f"  {path}")

    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s). See CONTRIBUTING.md for the rules.")
        return 1
    print(f"Structure OK ({len(files)} tracked files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

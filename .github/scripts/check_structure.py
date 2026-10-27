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
URL_RE = re.compile(r"^https?://\S+$")
# Paths that only exist on one person's machine.
LOCAL_PATH_RE = re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/]|/Users/|/home/|\\\\")
MAX_BYTES = 1_000_000

ACTIVITY_KEYS = ("author", "type", "title", "content")
CHAT_ROLES = {"user", "assistant"}

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

    for path in files:
        top = path.parts[0]
        if len(path.parts) == 1:
            if top not in ROOT_FILES:
                fail(path, "not an allowed top-level file (see CONTRIBUTING.md)")
        elif top not in ROOT_DIRS:
            fail(path, "not inside an allowed top-level folder (see CONTRIBUTING.md)")

        text = check_text(path, (ROOT / path).read_bytes())
        if text is None or top not in SECTIONS:
            if path.name.endswith(".md") and text is not None:
                check_markdown(path, text)
            continue

        seen_sections.add(top)
        if len(path.parts) != 2:
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

    for section in SECTIONS:
        if section not in seen_sections or not (ROOT / section / "README.md").is_file():
            fail(Path(section), "section is missing its README.md")

    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s). See CONTRIBUTING.md for the rules.")
        return 1
    print(f"Structure OK ({len(files)} tracked files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

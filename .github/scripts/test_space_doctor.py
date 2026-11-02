#!/usr/bin/env python3
"""Exercise the space doctor against small, committed Git repositories."""

import json
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).parent
DAY = 24 * 3600


class SpaceDoctorTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.git("init", "--quiet")
        for script in ("check_structure.py", "space_doctor.py"):
            self.write(f".github/scripts/{script}", (SCRIPTS / script).read_text(encoding="utf-8"))
        self.write("Chat/README.md", "# Chat\n")
        self.write("Chat/project/README.md", self.readme())
        self.write("Chat/project/output/one-pager.md", "# Project\n")
        # An hour old, so later commits in a test are clearly newer.
        self.commit(age=3600)

    def git(self, *args, age=0):
        stamp = f"{int(time.time() - age)} +0000"
        env = dict(os.environ, GIT_AUTHOR_DATE=stamp, GIT_COMMITTER_DATE=stamp)
        return subprocess.run(
            ["git", "-c", "user.name=test", "-c", "user.email=test@example.com", *args],
            cwd=self.root, check=True, capture_output=True, text=True, env=env,
        )

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def commit(self, age=0):
        self.git("add", ".")
        self.git("commit", "--quiet", "--allow-empty", "-m", "change", age=age)

    def readme(self, status="Open", owner="suraj"):
        return (
            f"# Project\n\n## Owner\n{owner}\n\n## Input\nResearch the project.\n"
            f"\n## Output format\nOne pager\n\n## Status\n{status}\n"
        )

    def tasks(self):
        result = subprocess.run(
            [sys.executable, str(self.root / ".github/scripts/space_doctor.py"), "--json"],
            cwd=self.root, check=True, capture_output=True, text=True,
        )
        return [(t["kind"], t["path"]) for t in json.loads(result.stdout)]

    def test_nothing_to_do(self):
        self.assertEqual(self.tasks(), [])

    def test_user_turn_needs_reply(self):
        self.write("Chat/project/chat.json", json.dumps(
            {"type": "conversation", "title": "Project", "messages": [{"role": "user", "content": "hi"}]}))
        self.write("Chat/project/chat.log.jsonl", '{"role": "assistant", "content": "hi"}\n')
        self.commit()
        self.assertEqual(self.tasks(), [])  # the log, not the .json, holds the latest turn
        self.write("Chat/project/chat.log.jsonl", '{"role": "user", "content": "and now?"}\n')
        self.commit()
        self.assertEqual(self.tasks(), [("reply", "Chat/project/chat.log.jsonl")])

    def test_inbox_file_is_sorted(self):
        self.write("Chat/notes.txt", "notes\n")
        self.commit()
        self.assertEqual(self.tasks(), [("sort-inbox", "Chat/notes.txt")])

    def test_done_sub_channel_is_folded(self):
        self.write("Chat/project/research/README.md", self.readme(status="Done"))
        self.commit()
        self.assertEqual(self.tasks(), [("fold", "Chat/project/research")])

    def test_new_input_needs_regeneration(self):
        self.write("Chat/project/inputs/brief.md", "# Brief\n")
        self.commit()
        self.assertEqual(self.tasks(), [("regenerate", "Chat/project/output/one-pager.md")])

    def test_missing_output(self):
        self.git("rm", "--quiet", "Chat/project/output/one-pager.md")
        self.commit()
        self.assertEqual(self.tasks(), [("missing-output", "Chat/project/output/one-pager.md")])

    def add_channel(self, name, age, **readme):
        self.write(f"Chat/{name}/README.md", self.readme(**readme))
        self.write(f"Chat/{name}/output/one-pager.md", "# Project\n")
        self.commit(age=age)

    def test_waiting_channel_takes_default_after_48_hours(self):
        self.add_channel("asked", DAY, status="Waiting")
        self.add_channel("asked-long-ago", 3 * DAY, status="Waiting")
        self.assertEqual(self.tasks(), [("default", "Chat/asked-long-ago")])

    def test_quiet_channel_goes_stale_unless_personal(self):
        self.add_channel("quiet", 15 * DAY)
        self.add_channel("suraj", 15 * DAY, owner="suraj")
        self.assertEqual(self.tasks(), [("stale", "Chat/quiet")])


if __name__ == "__main__":
    unittest.main()

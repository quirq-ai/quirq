#!/usr/bin/env python3
"""Exercise the structure checker against small, tracked Git repositories."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER = Path(__file__).with_name("check_structure.py")


class StructureCheckerTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.git("init", "--quiet")
        self.write(".github/scripts/check_structure.py", CHECKER.read_text(encoding="utf-8"))
        for section in ("Activity", "Chat", "Insights", "Library", "Vision"):
            self.write(f"{section}/README.md", f"# {section}\n")
        self.write("Vision/project-plan.md", "# Project plan\n")
        self.write("Chat/project/README.md", self.readme())
        self.write("Chat/project/research/README.md", self.readme(owner=True))

    def git(self, *args):
        return subprocess.run(
            ["git", *args], cwd=self.root, check=True, capture_output=True, text=True
        )

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def readme(self, output_format="One pager", status="Open", owner=False):
        text = (
            "# Project\n\n## Input\nResearch the project.\n"
            f"\n## Output format\n{output_format}\n\n## Status\n{status}\n"
        )
        if owner:
            text += "\n## Owner\nresearch-agent\n"
        return text

    def run_checker(self):
        # Staging is enough for git ls-files; no commit or Git identity is needed.
        self.git("add", ".")
        return subprocess.run(
            [sys.executable, str(self.root / ".github/scripts/check_structure.py")],
            cwd=self.root,
            capture_output=True,
            text=True,
        )

    def assert_problem(self, expected):
        result = self.run_checker()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(expected, result.stdout)
        self.assertIn("1 problem(s).", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_valid_layout(self):
        outputs = {
            "Slides": ("slides.md", "# Project\n\n---\n\n# Next slide\n"),
            "One pager": ("one-pager.md", "# Project\n"),
            "Website": ("index.html", "<html><body>Project</body></html>\n"),
            "GitHub URL": ("github.url", "https://github.com/quirq-ai/quirq\n"),
        }
        for output_format, (filename, content) in outputs.items():
            for status in ("Open", "Done"):
                with self.subTest(output_format=output_format, status=status):
                    output = self.root / "Chat/project/output"
                    if output.exists():
                        shutil.rmtree(output)
                    self.write("Chat/project/README.md", self.readme(output_format, status))
                    self.write(f"Chat/project/output/{filename}", content)
                    result = self.run_checker()
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertIn("Structure OK", result.stdout)
                    self.assertEqual(result.stderr, "")

    def test_sub_channel_requires_owner(self):
        self.write("Chat/project/research/README.md", self.readme())
        self.assert_problem(
            'Chat/project/research/README.md: sub-channel README needs an "## Owner" section'
        )

    def test_output_format_must_be_supported(self):
        self.write("Chat/project/README.md", self.readme(output_format="PDF"))
        self.assert_problem(
            "Chat/project/README.md: output format 'PDF' is not one of "
            "Slides, One pager, Website, GitHub URL"
        )

    def test_status_must_be_open_or_done(self):
        self.write("Chat/project/README.md", self.readme(status="In progress"))
        self.assert_problem('Chat/project/README.md: "## Status" must be Open or Done')

    def test_content_filename_must_be_kebab_case(self):
        (self.root / "Vision/project-plan.md").rename(self.root / "Vision/Project_Plan.md")
        self.assert_problem("Vision/Project_Plan.md: file names are lowercase kebab-case")


if __name__ == "__main__":
    unittest.main()

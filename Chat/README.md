# Chat

Every task gets a folder here, grouped by person:

```
Chat/<username>/tasks/<task-name>/
  README.md     "## Goal" (what you want) and "## Output format"
  chats/        saved conversations about the task
  outcome/      what Claude generates from the goal and the chats
```

You write the goal and pick an output format: Slides, One pager, Website, or GitHub URL. The project's conversations are stored in `chats/`, and Claude writes the result to `outcome/` in that format (`slides.md`, `one-pager.md`, `index.html`, or `github.url`). `<username>` is the person's GitHub login in lowercase, and `<task-name>` is lowercase kebab-case.

Start with sharmasuraj0123/tasks/getting-started/. Saved chats are read-only in the app and do not call a model. File links are relative to the repository root. The full rules are in CONTRIBUTING.md.

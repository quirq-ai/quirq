# Chat

Saved conversations, grouped by person and then by task:

```
Chat/<username>/tasks/<task-name>/
  README.md     "## Purpose" (what the task is for) and "## Output format"
  index.json    the saved conversation
```

The output format is one of Slides, One pager, Website, or GitHub URL. `<username>` is the person's GitHub login in lowercase, and `<task-name>` is lowercase kebab-case. Start with sharmasuraj0123/tasks/getting-started/index.json. Edit its messages on disk to change the view. Conversations are read-only and do not call a model or generate replies. File links are relative to the repository root.

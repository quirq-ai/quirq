# Chat

Every task gets a folder here, grouped by person:

```
Chat/<username>/
  <any file>    drop files here; Claude sorts them into tasks
  tasks/<task-name>/
    README.md   "## Goal" (what you want) and "## Output format"
    chats/      saved conversations about the task
    sources/    files sorted in from the inbox
    outcome/    what Claude generates from all of the above
```

You write the goal and pick an output format: Slides, One pager, Website, or GitHub URL. The project's conversations are stored in `chats/`, and Claude writes the result to `outcome/` in that format (`slides.md`, `one-pager.md`, `index.html`, or `github.url`). Drop any file straight into your username folder and Claude will sort it into a task, merging tasks where they overlap so the list stays short. `<username>` is the person's GitHub login in lowercase, and `<task-name>` is lowercase kebab-case.

Start with sharmasuraj0123/tasks/getting-started/. Saved chats are read-only in open-chat. On the hub, members can add to a conversation, and the new turns land in a `.log.jsonl` beside its `.json`. File links are relative to the repository root. The full rules are in CONTRIBUTING.md.

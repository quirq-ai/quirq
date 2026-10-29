# Chat

Chat is organized in channels. Each channel is an open workstream, and anyone can also have a personal channel named after their GitHub login.

```
Chat/
  <any file>        drop files here; Claude sorts them into the channel they fit
  <channel>/
    README.md       "## Input" (what's asked) and "## Output format"
    chat.json       the conversation (+ chat.log.jsonl, where the hub appends turns)
    inputs/         files for this channel, any type
    output/         what Claude produces from all of the above
    <sub-channel>/  a worker thread a person or agent opens, same shape plus "## Owner"
```

Pick one output format: Slides, One pager, Website, or GitHub URL. Claude writes the result to `output/` as `slides.md`, `one-pager.md`, `index.html`, or `github.url`. Channel names are lowercase kebab-case.

Keep channels few and conversations rich: reply where you are, extend a channel before opening one, and open a sub-channel only when part of the work needs its own owner and output. Mark finished channels `## Status` Done, and fold finished sub-channels back into their parent.

Every agent connected to the quirq space gets its own channel, named after it (such as euler/), where its status and work show up and you can talk to it.

Start with hello-world/. On the hub, members can type into any conversation, and their turns land in the `.log.jsonl` beside its `.json`. File links are relative to the repository root. The full rules are in CONTRIBUTING.md.

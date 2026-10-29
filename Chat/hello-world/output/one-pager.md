# Getting started with quirq

quirq is a filesystem-first workspace. Files hold the content and open-chat shows it, so changing a file changes what you see.

## How work flows

1. **Open a channel.** Each workstream is a channel in `Chat/<channel>/`, and everyone can have a personal one. Its README states the input and picks one output format: Slides, One pager, Website, or GitHub URL.
2. **Talk it through.** The channel's conversation is `chat.json`, and files for it go in `inputs/`.
3. **Get the output.** Claude reads the input, the conversation, and the files, then writes the result to `output/` in the chosen format.

## The other places

- **Activity** records what happened.
- **Insights** keeps the observations worth returning to.
- **Vision** holds the direction behind the work.
- **Library** saves links to outside pages.

## Next step

Say hello in this channel, or open a channel with an input and an output format and start talking.

# Example Workflow

User: `jimeng-video outline — 校园新人第一天报到，轻松青春感。`

Assistant creates the full story only. User approves it.

User: `jimeng-video split`

Assistant splits at natural beats, defaulting to 15 seconds, and records Beginning/Ending State for every part.

User: `jimeng-video prompt 3`

Assistant:
1. Reads Part 3 plus Part 2 ending and Part 4 beginning when available.
2. Runs Cost Guard.
3. Creates the first-frame image prompt.
4. Delegates final motion-prompt wording to `jimeng-prompt-image2video` when installed.
5. Re-checks returned wording against continuity and cost risk.
6. Returns only the selected production block.

Recommended output:

```text
Part 03 — 15s

First-frame image prompt:
...

Jimeng image-to-video prompt:
...

Generation risk: LOW
```

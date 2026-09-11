# Upstream Prompt Skill Integration

Preferred upstream package:

`full-aigc-skills/jimeng-skills`

Install all skills:

```bash
npx skills add full-aigc-skills/jimeng-skills
```

Or install only the image-to-video prompt skill when supported by the installer:

```bash
npx skills add full-aigc-skills/jimeng-skills --skill jimeng-prompt-image2video
```

## Delegation boundary

`jimeng-video` remains the director. It owns:
- story outline
- 15-second segmentation
- continuity
- first-frame requirements
- Cost Guard
- deciding whether a story beat is too risky

`jimeng-prompt-image2video` is the prompt specialist. Give it only:
- the selected segment's story purpose
- beginning state
- ending state
- allowed actions
- camera intent
- reference-image facts
- explicit constraints produced by Cost Guard

Do not ask the upstream skill to rewrite the whole story or repartition segments. After it returns a prompt, re-check continuity and risk before presenting it.

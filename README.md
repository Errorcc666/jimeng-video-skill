# jimeng-video-skill

Agent Skill for planning story-driven Jimeng (即梦) image-to-video workflows, with natural 15-second segmentation, continuity tracking, and a Cost Guard designed to reduce avoidable Jimeng regenerations.

## Workflow

Story idea / reference image → outline → natural 15-second clips → continuity check → first-frame prompt → Jimeng video prompt → Cost Guard → human review → Jimeng generation.

## Features

- Default 15-second clips; duration can be overridden.
- Split on natural narrative beats rather than mechanical timing cuts.
- Track beginning/ending states between adjacent clips.
- Separate first-frame image prompts from image-to-video prompts.
- Classify generation risk as LOW / MEDIUM / HIGH.
- Automatically simplify HIGH-risk clips unless the user explicitly opts out.
- Optional integration with `full-aigc-skills/jimeng-skills` for Jimeng-specific prompt wording.

## Install

```bash
npx skills add Errorcc666/jimeng-video-skill --skill jimeng-video
```

Recommended companion skill:

```bash
npx skills add full-aigc-skills/jimeng-skills --skill jimeng-prompt-image2video
```

## Usage

```text
jimeng-video outline
jimeng-video split
jimeng-video split --seconds 10
jimeng-video prompt 3
```

## Design principle

This project does not try to minimize GPT token usage. Its priority is minimizing expensive or avoidable Jimeng video regeneration by spending more reasoning before generation.

## License

MIT.

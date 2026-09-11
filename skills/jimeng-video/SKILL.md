---
name: jimeng-video
summary: Plan story-driven Jimeng image-to-video clips with 15-second defaults and generation-cost safeguards.
description: Use when turning a story idea, reference image, or approved outline into Jimeng (即梦) video segments, especially when expensive regenerations should be minimized.
---

# Jimeng Video

## Goal

Use GPT reasoning generously before generation so Jimeng is asked to render fewer, safer, more coherent clips. **Default clip duration: 15 seconds.** Do not call Jimeng automatically unless the user explicitly asks for execution.

## Commands

### `jimeng-video outline`
Create or refine the full story outline. Story length is not fixed. Return only the production-relevant story structure: premise, characters, setting, beginning, development, turn/conflict, ending, and an estimated number of 15-second clips.

### `jimeng-video split [--seconds N]`
Split an approved outline at natural story beats; default `N=15`. A clip may be shorter when the beat naturally ends. Read `references/segment-template.md`. Every segment must include `Beginning State` and `Ending State`; adjacent states must be compatible.

### `jimeng-video prompt <part>`
Create the first-frame image prompt plus the Jimeng image-to-video prompt for one selected segment. Read `references/segment-template.md`, `references/cost-guard.md`, and `references/upstream-integration.md`.

If the installed skill `jimeng-prompt-image2video` is available, delegate **only the final image-to-video prompt drafting** to it after this skill has locked story intent, continuity, and risk constraints. Then apply this skill's Cost Guard to the returned prompt. If that upstream skill is unavailable, use `references/local-prompt-fallback.md`.

## Production Contract

A 15-second segment should normally contain **one primary story event** and no more than **two supporting actions**. Preserve character identity, hairstyle, clothing, accessories, props, spatial position, posture, expression, scene, lighting/time, and camera continuity whenever relevant.

The previous segment's `Ending State` is the next segment's `Beginning State`. Do not silently reset positions, props, clothing, time, or emotional state.

## Cost Guard

Before returning any Jimeng prompt, rate it `LOW`, `MEDIUM`, or `HIGH`. High-risk causes include overloaded action chains, precise hand/object interactions, several people acting independently, fast scene changes, difficult body mechanics, contradictory camera instructions, or continuity breaks. For `HIGH`, simplify first and return the safer prompt unless the user explicitly asks to preserve the risky version.

## Output Rule

Final prompts must be directly copyable. Do not bury them under explanations. If the user asks for one segment, do not regenerate the entire outline or every segment.

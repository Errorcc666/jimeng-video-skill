# Local Image-to-Video Prompt Fallback

Use only when `jimeng-prompt-image2video` is unavailable.

Build the prompt in this order:

1. **Subject + starting state** — identify visible subject(s) and their exact starting posture/position.
2. **Primary motion** — one clear action described chronologically.
3. **Supporting reaction** — at most one or two simple reactions.
4. **Environment motion** — only if visible and useful (hair, fabric, leaves, light, background people).
5. **Camera** — one coherent instruction: static, slow push, slow pull, pan, track, or gentle handheld.
6. **Ending state** — where the subject and camera should end.
7. **Stability constraints** — preserve identity, clothing, scene, object count, and visual style.

Prefer concrete motion verbs over cinematic adjectives. Avoid describing invisible backstory inside the generation prompt.

### Compact example

`The woman begins standing beside the classroom desk, holding two books against her chest. She glances toward the seated students, gives a small nervous smile, then takes two slow steps forward. Her hair and skirt move naturally with the motion. The camera makes a gentle forward push at eye level and ends in a medium shot. Keep her face, outfit, classroom layout and book count consistent; no scene change.`

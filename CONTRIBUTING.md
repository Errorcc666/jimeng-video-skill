# Contributing

Contributions are welcome when they improve Jimeng production reliability, continuity handling, prompt quality, or documentation without turning the skill into a large automation framework.

## Principles

- Keep `SKILL.md` compact and operational.
- Put detailed guidance in `references/`.
- Preserve the default 15-second workflow unless a change is explicitly configurable.
- Prefer fewer, safer video generations over more elaborate prompt text.
- Do not bundle proprietary Jimeng code, credentials, cookies, or session data.

## Before opening a pull request

Run:

```bash
python3 tests/validate_skill.py
```

Describe the production problem being solved and include a before/after example when changing prompt or continuity behavior.

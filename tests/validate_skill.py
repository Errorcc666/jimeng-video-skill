from pathlib import Path
import re

repo = Path(__file__).resolve().parents[1]
skill = repo / "skills" / "jimeng-video"
required = [
    repo / "README.md",
    repo / "README.zh-CN.md",
    repo / "LICENSE",
    repo / "CONTRIBUTING.md",
    skill / "SKILL.md",
    skill / "references" / "segment-template.md",
    skill / "references" / "cost-guard.md",
    skill / "references" / "upstream-integration.md",
    skill / "references" / "local-prompt-fallback.md",
    skill / "templates" / "workflow-example.md",
]
missing = [str(p.relative_to(repo)) for p in required if not p.exists()]
assert not missing, f"Missing: {missing}"

text = (skill / "SKILL.md").read_text(encoding="utf-8")
assert text.startswith("---\n"), "SKILL.md must start with YAML frontmatter"
assert re.search(r"name:\s*jimeng-video", text), "skill name missing"
assert re.search(r"description:\s*Use when", text), "discovery description missing"
assert re.search(r"default.*15", text, re.I), "15-second default missing"
assert "jimeng-prompt-image2video" in text, "upstream delegation missing"
assert "Cost Guard" in text, "Cost Guard missing"
assert "Ending State" in text and "Beginning State" in text, "continuity contract missing"
for command in ("outline", "split", "prompt"):
    assert command in text, f"{command} command missing"

word_count = len(text.split())
assert word_count < 500, f"SKILL.md too large: {word_count} words"
print(f"PASS: GitHub-ready jimeng-video skill validated ({word_count} words)")

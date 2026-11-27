"""Manifest consistency: skill folders match SKILL.md names, agent names match,
plugin.json version matches pyproject and CHANGELOG."""
import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_skill_count_and_names():
    skills = sorted(os.listdir(os.path.join(ROOT, "skills")))
    assert len(skills) == 36, skills
    for name in skills:
        text = open(os.path.join(ROOT, "skills", name, "SKILL.md")).read()
        assert f"name: {name}" in text, name
        assert "## " in text and len(text) > 500, name

def test_agent_names_and_models():
    agents = sorted(os.listdir(os.path.join(ROOT, "agents")))
    assert len(agents) == 20, agents
    for fname in agents:
        text = open(os.path.join(ROOT, "agents", fname)).read()
        assert f"name: {fname[:-3]}" in text, fname
        assert "model: " in text, fname
        assert "Background mein kaam" in text, fname

def test_version_matches():
    plugin = json.load(open(os.path.join(ROOT, ".claude-plugin/plugin.json")))
    pyproject = open(os.path.join(ROOT, "pyproject.toml")).read()
    assert plugin["version"] in pyproject
    assert plugin["version"] in open(os.path.join(ROOT, "CHANGELOG.md")).read()

def test_hub_lists_scratch_flow_and_commands():
    hub = open(os.path.join(ROOT, "skills/webdev/SKILL.md")).read()
    for cmd in ("/webdev build", "/webdev audit", "/webdev redesign", "/webdev fix",
                "/webdev page", "/webdev speed", "/webdev launch"):
        assert cmd in hub, cmd
    assert "Scratch se nayi website" in hub
    assert "Background agents" in hub

def test_usage_has_scratch_examples():
    usage = open(os.path.join(ROOT, "docs/USAGE.md")).read()
    assert "home cleaning" in usage.lower()
    assert "dukaan" in usage.lower()
    assert "website banao" in usage

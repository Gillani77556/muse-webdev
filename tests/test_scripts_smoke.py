"""Smoke tests: launcher doctor works; each script has a usage docstring."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_doctor():
    out = subprocess.run([sys.executable, os.path.join(ROOT, "scripts/webdev"), "doctor"],
                         capture_output=True, text=True, timeout=30)
    assert out.returncode == 0
    assert json.loads(out.stdout)["ready"] is True

def test_scripts_have_docstrings():
    for fname in sorted(os.listdir(os.path.join(ROOT, "scripts"))):
        if fname.endswith(".py"):
            text = open(os.path.join(ROOT, "scripts", fname)).read()
            assert '"""' in text, fname

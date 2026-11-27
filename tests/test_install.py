"""Install test: a clean install must ship the scripts launcher.

Regression test for the 27 Nov 2026 live-test failure: install.sh copied
skills and agents but not scripts/, so
  ~/.claude/skills/webdev/scripts/webdev doctor
did not exist after install. Run with pytest; stdlib only otherwise.
"""
import json, os, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_clean_install_ships_scripts_and_doctor():
    with tempfile.TemporaryDirectory() as home:
        env = dict(os.environ, HOME=home)
        out = subprocess.run(["bash", "install.sh"], cwd=ROOT, env=env,
                             capture_output=True, text=True, timeout=120)
        assert out.returncode == 0, out.stdout + out.stderr
        launcher = os.path.join(home, ".claude/skills/webdev/scripts/webdev")
        assert os.path.isfile(launcher), "scripts/webdev missing after install"
        out = subprocess.run([sys.executable, launcher, "doctor"],
                             capture_output=True, text=True, timeout=30)
        assert out.returncode == 0, out.stdout + out.stderr
        assert json.loads(out.stdout)["ready"] is True
        assert len(os.listdir(os.path.join(home, ".claude/skills"))) >= 36
        assert len([f for f in os.listdir(os.path.join(home, ".claude/agents"))
                    if f.startswith("webdev-")]) == 20

"""Install the built wheel and run its CLI outside the source checkout."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
wheels = list((root / "dist").glob("*.whl"))
assert len(wheels) == 1, "Expected one wheel"
subprocess.run([sys.executable, "-m", "pip", "install", "--force-reinstall", "--no-deps", str(wheels[0])], check=True)
with tempfile.TemporaryDirectory() as directory:
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    result = subprocess.run(
        ["change-log-creator", "-r", str(root), "-c", "1"],
        cwd=directory, env=env, capture_output=True, text=True, check=True,
    )
    assert "# CHANGE LOG" in result.stdout
    assert result.stdout.count(" Change: ") == 1
print("Installed wheel CLI passed outside checkout")

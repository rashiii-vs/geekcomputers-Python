import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TEST_FILE = ROOT / "work" / "R25-T045" / "test_ping_subnet.py"

if os.name == "nt":
    VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
else:
    VENV_PYTHON = ROOT / ".venv" / "bin" / "python"

if VENV_PYTHON.exists():
    PYTHON = str(VENV_PYTHON)
else:
    PYTHON = sys.executable

if not TEST_FILE.is_file():
    print("ERROR: Test file not found:", TEST_FILE)
    sys.exit(1)

print("Running R25-T045 tests...")
print("Python executable:", PYTHON)
print("Test file:", TEST_FILE)

result = subprocess.run(
    [
        PYTHON,
        "-m",
        "pytest",
        "-v",
        str(TEST_FILE),
    ],
    cwd=str(ROOT),
)

sys.exit(result.returncode)

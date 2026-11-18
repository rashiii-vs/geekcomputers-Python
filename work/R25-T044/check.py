
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

PYTHON = ROOT / ".venv" / "bin" / "python"

TEST_FILE = ROOT / "work" / "R25-T044" / "test_personal_translator.py"

result = subprocess.run(
    [
        str(PYTHON),
        "-m",
        "pytest",
        str(TEST_FILE),
        "-v",
    ],
    cwd=ROOT,
)

sys.exit(result.returncode)

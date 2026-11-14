import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEST_FILE = ROOT / "work" / "R25-T041" / "test_contract.py"

result = subprocess.run(
    [
        sys.executable,
        "-m",
        "pytest",
        "-q",
        str(TEST_FILE),
    ],
    cwd=ROOT,
)

raise SystemExit(result.returncode)

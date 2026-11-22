import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TEST_FILE = ROOT / "work" / "R25-T043" / "test_dec_to_hex.py"


def main():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-v",
            str(TEST_FILE),
        ],
        cwd=ROOT,
    )

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())

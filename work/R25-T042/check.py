import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TASK_DIR = ROOT / "work" / "R25-T042"
TEST_FILE = TASK_DIR / "test_contract.py"
EVIDENCE_FILE = TASK_DIR / "run_evidence.txt"

command = [
    sys.executable,
    "-m",
    "pytest",
    "-v",
    str(TEST_FILE),
]

print("Running focused tests:")
print(" ".join(command))

result = subprocess.run(
    command,
    cwd=ROOT,
    capture_output=True,
    text=True,
)

output = result.stdout + result.stderr
print(output)

match = re.search(r"(\d+) passed", output)
passed_count = int(match.group(1)) if match else 0

pytest_version = subprocess.run(
    [sys.executable, "-m", "pytest", "--version"],
    capture_output=True,
    text=True,
)

git_version = subprocess.run(
    ["git", "--version"],
    capture_output=True,
    text=True,
)

evidence = f"""R25-T042 Test Run Evidence

Actual command:
python3 work/R25-T042/check.py

Internal test command:
{' '.join(command)}

Tests passed: {passed_count}
Exit status: {result.returncode}

Python version: {sys.version.split()[0]}
Pytest version: {pytest_version.stdout.strip()}
Git version: {git_version.stdout.strip()}

Actual test output:
{output}
"""

EVIDENCE_FILE.write_text(evidence)
print(f"Evidence saved to: {EVIDENCE_FILE}")

sys.exit(result.returncode)

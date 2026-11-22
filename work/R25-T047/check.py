import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from friday import friday


tests = [
    ("smallest matching input", "runnotepad", True),
    ("ordinary matching input", "please run Notepad", True),
    ("different application", "open calculator", False),
    ("Notepad without an action", "Notepad", False),
]

for name, command, expected in tests:
    actual = friday(command)

    print(f"Test: {name}")
    print(f"Input: {command!r}")
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")

    assert actual == expected, f"FAILED: {name}"
    print("Result: PASS")
    print()

print("All regression checks passed.")

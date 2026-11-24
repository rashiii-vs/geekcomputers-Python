from pathlib import Path
import pytest
import sys

ROOT = Path(__file__).resolve().parents[2]
TEST_FILE = Path(__file__).with_name("test_totaldigits.py")

sys.path.insert(0, str(ROOT))

if __name__ == "__main__":
    sys.exit(pytest.main(["-v", str(TEST_FILE)]))

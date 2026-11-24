from pathlib import Path
import pytest

TEST_FILE = Path(__file__).with_name("test_string_rotation.py")

if __name__ == "__main__":
    raise SystemExit(pytest.main(["-v", str(TEST_FILE)],))

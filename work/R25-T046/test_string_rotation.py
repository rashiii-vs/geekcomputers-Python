import importlib.util
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import builtins

MODULE_PATH = Path(__file__).resolve().parents[2] / "string_rotation.py"

spec = importlib.util.spec_from_file_location("string_rotation", MODULE_PATH)
rotation_module = importlib.util.module_from_spec(spec)

# The original module asks for input when imported.
original_input = builtins.input
builtins.input = lambda: "Tie"
try:
    spec.loader.exec_module(rotation_module)
finally:
    builtins.input = original_input

# Source: string_rotation.py, original lines 9-10.
# Empty input prints [] and returns None.

def test_empty_string():
    output = StringIO()
    with redirect_stdout(output):
        result = rotation_module.rotate("")
    assert output.getvalue().strip() == "[]"
    assert result is None

# Source: string_rotation.py, original lines 12-15.
# Each iteration rotates once, joins the characters, and prints the list.

def test_tie_rotations():
    output = StringIO()
    with redirect_stdout(output):
        result = rotation_module.rotate("Tie")
    assert output.getvalue().strip() == "['ieT', 'eTi', 'Tie']"
    assert result is None

# Source: string_rotation.py, original lines 8 and 13.
# The input is a character list and the rotation creates a new list.

def test_rotate_left_once():
    characters = ["T", "i", "e"]
    result = rotation_module._rotate_left_once(characters)

    assert result == ["i", "e", "T"]
    assert characters == ["T", "i", "e"]

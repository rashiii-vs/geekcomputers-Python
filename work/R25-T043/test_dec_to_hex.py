import builtins
import runpy
from unittest.mock import patch
from pathlib import Path


SOURCE = Path(__file__).resolve().parents[2] / "dec_to_hex.py"


def reference_hex(number):
    digits = "0123456789abcdef"

    if number == 0:
        return "0x0"

    sign = "-" if number < 0 else ""
    number = abs(number)
    result = ""

    while number:
        remainder = number % 16
        result = digits[remainder] + result
        number //= 16

    return sign + "0x" + result


def run_script(input_value):
    printed = []

    with patch.object(builtins, "input", return_value=input_value):
        with patch.object(builtins, "print", side_effect=printed.append):
            namespace = runpy.run_path(str(SOURCE))

    return printed, namespace


def test_decimal_to_hex():
    test_cases = [
        ("0", "0x0"),
        ("1", "0x1"),
        ("2", "0x2"),
        ("3", "0x3"),
        ("4", "0x4"),
        ("5", "0x5"),
        ("6", "0x6"),
        ("7", "0x7"),
        ("8", "0x8"),
        ("9", "0x9"),
        ("10", "0xa"),
        ("11", "0xb"),
        ("12", "0xc"),
        ("13", "0xd"),
        ("14", "0xe"),
        ("15", "0xf"),
        ("16", "0x10"),
        ("17", "0x11"),
        ("18", "0x12"),
        ("19", "0x13"),
        ("-1", "-0x1"),
        ("-2", "-0x2"),
        ("-10", "-0xa"),
        ("42", "0x2a"),
    ]

    for value, expected in test_cases:
        independently_calculated = reference_hex(int(value))
        assert independently_calculated == expected

        actual, namespace = run_script(value)

        assert len(actual) == 1
        assert isinstance(actual[0], str)
        assert actual == [expected], (
        f"Input: {value}, expected: {expected}, actual: {actual}"
        )
        assert namespace["dec_num"] == value


if __name__ == "__main__":
    test_decimal_to_hex()

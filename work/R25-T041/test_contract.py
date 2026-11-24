
import importlib.util
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[2] / (
    "solution to euler project problem 10.py"
)

spec = importlib.util.spec_from_file_location("problem10", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


# Source lines 8 and 15–19:
# The intended function accepts a positive integer.
# Input 1 is the smallest positive integer.
# There are no primes below 1, so the expected sum is 0.
def test_smallest_positive_input():
    actual = module.solution(1)
    expected = 0
    assert actual == expected, f"Input: 1, expected: {expected}, actual: {actual}"


# Source line 5:
# 2 + 3 + 5 + 7 = 17.
def test_ordinary_input():
    actual = module.solution(10)
    expected = 17
    assert actual == expected, f"Input: 10, expected: {expected}, actual: {actual}"


# Source lines 16–19:
# The function sums primes strictly below n.
# There are no primes below 2.
def test_prime_boundary():
    actual = module.solution(2)
    expected = 0
    assert actual == expected, f"Input: 2, expected: {expected}, actual: {actual}"

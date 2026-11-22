from totaldigits import totaldigits


def test_totaldigits_zero():
    assert totaldigits(0) == 1


def test_totaldigits_ordinary_number():
    assert totaldigits(12345) == 5

def test_totaldigits_negative_number():
    assert totaldigits(-123) == 3

def test_totaldigits_single_digit():
    assert totaldigits(7) == 1


def test_totaldigits_large_number():
    assert totaldigits(123456789012345) == 15

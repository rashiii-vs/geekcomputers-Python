
import multiple_comditions


def test_smallest_valid_input(capsys):
    # Source lines 3-5: integer input and the branch for choice 1.
    choice = 1
    expected = "in first if"

    multiple_comditions.check_condition(choice)

    actual = capsys.readouterr().out.strip()
    assert actual == expected


def test_ordinary_valid_input(capsys):
    # Source lines 3, 6-7: integer input and the branch for choice 2.
    choice = 2
    expected = "in second if"

    multiple_comditions.check_condition(choice)

    actual = capsys.readouterr().out.strip()
    assert actual == expected

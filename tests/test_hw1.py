"""Test cases are important."""


from homework1 import hw1


def test_return_number_3():
    """Make sure the return of the function is 3, integer"""

    assert hw1.return_number_3() == 3


def test_return_string_vcu():
    """Make sure the return of the function is the string vcu"""

    assert hw1.return_string_vcu() == "vcu"


def test_return_lowercased_string():
    """Make sure the return of the function is the lowercased version of the parameter."""

    assert hw1.return_lowercased_string("HI THERE MOM") == "hi there mom"
    assert hw1.return_lowercased_string("vcu.edu") == "vcu.edu"
    assert (
        hw1.return_lowercased_string("We Wish You a Merry Monday")
        == "we wish you a merry monday"
    )


def test_return_without_starting_ending_whitespace():
    """Make sure the function strips the whitespace """

    assert (
        hw1.return_without_starting_ending_whitespace("   asdfasdf    ") == "asdfasdf"
    )


def test_return_addition():
    """ Make sure the function returns the sum of the two parameters. """

    assert hw1.return_addition(1, 2) == 3
    assert hw1.return_addition(100, 200) == 300
    assert hw1.return_addition(43, 43) == 86
    assert hw1.return_addition(50, 25) == 75
    assert hw1.return_addition(19, -19) == 0

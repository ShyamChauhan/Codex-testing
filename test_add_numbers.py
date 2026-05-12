from add_numbers import add_two_numbers


def test_add_two_positive_numbers():
    assert add_two_numbers(2, 3) == 5


def test_add_two_negative_numbers():
    assert add_two_numbers(-4, -6) == -10


def test_add_positive_and_negative_number():
    assert add_two_numbers(10, -3) == 7

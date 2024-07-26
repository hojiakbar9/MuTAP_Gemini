def truncate_number(number: float) -> float:

    return number % 1.0


# <test>


def test():
    assert truncate_number(1.5) == 0.5
    assert truncate_number(1.0) == 0.0
    assert truncate_number(2.0) == 0.0
    assert truncate_number(3.14) == 0.14
    assert truncate_number(-2.5) == -0.5


# </test>

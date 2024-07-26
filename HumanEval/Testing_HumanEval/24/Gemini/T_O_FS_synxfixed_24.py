def largest_divisor(n: int) -> int:

    for i in reversed(range(n)):
        if n % i == 0:
            return i


# <test>


def test():
    assert largest_divisor(12) == 6
    assert largest_divisor(15) == 5
    assert largest_divisor(7) == 1


# </test>

#<test>

def test():
    assert largest_divisor(12) == 6
    assert largest_divisor(15) == 5
    assert largest_divisor(7) == 1
#</test>

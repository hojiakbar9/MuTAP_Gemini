def greatest_common_divisor(a: int, b: int) -> int:

    while b:
        a, b = b, a % b
    return a


# <test>


def test():
    assert greatest_common_divisor(15, 25) == 5
    assert greatest_common_divisor(20, 10) == 10
    assert greatest_common_divisor(10, 15) == 5


# </test>

#<test>

def test():
    assert greatest_common_divisor(15, 25) == 5
    assert greatest_common_divisor(20, 10) == 10
    assert greatest_common_divisor(10, 15) == 5
#</test>

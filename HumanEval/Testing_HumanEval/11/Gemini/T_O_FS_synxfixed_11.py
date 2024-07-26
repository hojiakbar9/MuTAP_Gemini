from typing import List


def string_xor(a: str, b: str) -> str:

    def xor(i, j):
        if i == j:
            return "0"
        else:
            return "1"

    return "".join(xor(x, y) for x, y in zip(a, b))


# <test>


def test():
    assert string_xor("1010", "0011") == "1001"
    assert string_xor("1111", "0000") == "1111"
    assert string_xor("0101", "1010") == "1111"


# </test>

#<test>

def test():
    assert string_xor("1010", "0011") == "1001"
    assert string_xor("1111", "0000") == "1111"
    assert string_xor("0101", "1010") == "1111"
#</test>

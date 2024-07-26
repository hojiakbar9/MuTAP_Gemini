def string_sequence(n: int) -> str:

    return " ".join([str(x) for x in range(n + 1)])


# <test>


def test():
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(1) == "0 1"
    assert string_sequence(0) == "0"


# </test>

#<test>

def test():
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(1) == '0 1'
    assert string_sequence(0) == '0'
#</test>

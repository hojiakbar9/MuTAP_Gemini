from typing import List


def concatenate(strings: List[str]) -> str:

    return "".join(strings)


def test():
    assert concatenate(["a", "b", "c"]) == "abc"
    assert concatenate(["", "b", ""]) == "b"
    assert concatenate(["1", "2", "3"]) == "123"


# </test>

#<test>

def test():
    assert concatenate(["a", "b", "c"]) == "abc"
    assert concatenate(["", "b", ""]) == "b"
    assert concatenate(["1", "2", "3"]) == "123"
#</test>

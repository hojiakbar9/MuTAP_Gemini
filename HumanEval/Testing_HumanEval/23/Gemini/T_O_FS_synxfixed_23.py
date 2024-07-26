def strlen(string: str) -> int:

    return len(string)


# <test>


def test():
    assert strlen("hello") == 5
    assert strlen("world") == 5
    assert strlen("") == 0


# </test>

#<test>

def test():
    assert strlen("hello") == 5
    assert strlen("world") == 5
    assert strlen("") == 0
#</test>

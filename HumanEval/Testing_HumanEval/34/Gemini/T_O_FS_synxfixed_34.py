def unique(l: list):

    return sorted(list(set(l)))


# <test>


def test():
    assert unique([1, 2, 3, 3, 2, 1]) == [1, 2, 3]
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique([1, 1, 1, 1, 1]) == [1]
    assert unique([]) == []


# </test>

#<test>

def test():
    assert unique([1, 2, 3, 3, 2, 1]) == [1, 2, 3]
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique([1, 1, 1, 1, 1]) == [1]
    assert unique([]) == []
#</test>

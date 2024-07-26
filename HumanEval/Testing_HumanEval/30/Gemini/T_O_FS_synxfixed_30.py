def get_positive(l: list):

    return [e for e in l if e > 0]


# <test>


def test():
    assert get_positive([1, 2, -3, 4, -5]) == [1, 2, 4]
    assert get_positive([-1, -2, -3, -4, -5]) == []
    assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert get_positive([0, 1, 2, 3, 4]) == [1, 2, 3, 4]
    assert get_positive([]) == []


# </test>

#<test>

def test():
    assert get_positive([1, 2, -3, 4, -5]) == [1, 2, 4]
    assert get_positive([-1, -2, -3, -4, -5]) == []
    assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert get_positive([0, 1, 2, 3, 4]) == [1, 2, 3, 4]
    assert get_positive([]) == []
#</test>

from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:

    return [x for x in values if isinstance(x, int)]


# <test>


def test():
    assert filter_integers([1, 2, "a", 3, 4.5]) == [1, 2, 3]
    assert filter_integers([1, "a", "b", 2.5, "c"]) == [1]
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert filter_integers([]) == []
    assert filter_integers([1.0, 2.0, 3.0, 4.0, 5.0]) == []


# </test>

#<test>

def test():
    assert filter_integers([1, 2, 'a', 3, 4.5]) == [1, 2, 3]
    assert filter_integers([1, 'a', 'b', 2.5, 'c']) == [1]
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert filter_integers([]) == []
    assert filter_integers([1.0, 2.0, 3.0, 4.0, 5.0]) == []
#</test>

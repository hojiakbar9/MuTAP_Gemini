from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:

    import collections

    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]


# <test>


def test():
    assert remove_duplicates([1, 1, 2, 3, 3, 4]) == [2, 4]
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([1, 1, 1, 2, 2, 2]) == []
    assert remove_duplicates([1, 2, 3, 1, 2, 3]) == []
    assert remove_duplicates([1, 2, 3, 1, 2, 3, 4]) == [4]


# </test>

#<test>

def test():
    assert remove_duplicates([1, 1, 2, 3, 3, 4]) == [2, 4]
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([1, 1, 1, 2, 2, 2]) == []
    assert remove_duplicates([1, 2, 3, 1, 2, 3]) == []
    assert remove_duplicates([1, 2, 3, 1, 2, 3, 4]) == [4]
#</test>

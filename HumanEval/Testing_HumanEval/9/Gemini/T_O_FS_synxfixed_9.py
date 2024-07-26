from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:

    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result


# <test>


def test():
    assert rolling_max([1, 3, 2, 5, 1]) == [1, 3, 3, 5, 5]
    assert rolling_max([10, 5, 10, 100, 1]) == [10, 10, 10, 100, 100]
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


# </test>

#<test>

def test():
    assert rolling_max([1, 3, 2, 5, 1]) == [1, 3, 3, 5, 5]
    assert rolling_max([10, 5, 10, 100, 1]) == [10, 10, 10, 100, 100]
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
#</test>

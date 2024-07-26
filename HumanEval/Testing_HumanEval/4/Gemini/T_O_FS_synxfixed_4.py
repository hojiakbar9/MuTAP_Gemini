from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:

    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


def test():
    assert mean_absolute_deviation([1.0, 2.0, 3.0]) == 0.6666666666666666
    assert mean_absolute_deviation([1.0, 1.0, 1.0]) == 0.0
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) == 1.2


# </test>s

#<test>

def test():
    assert mean_absolute_deviation([1.0, 2.0, 3.0]) == 0.6666666666666666
    assert mean_absolute_deviation([1.0, 1.0, 1.0]) == 0.0
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) == 1.2
#</test>

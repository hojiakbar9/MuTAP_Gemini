from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:

    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]


# <test>


def test():
    assert rescale_to_unit([1.0, 2.0, 3.0]) == [0.0, 0.5, 1.0]
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([10.0, 20.0, 30.0]) == [0.0, 0.5, 1.0]
    assert rescale_to_unit([1.0, 1.0, 1.0]) == [0.0, 0.0, 0.0]
    assert rescale_to_unit([1.0, -2.0, 3.0, -4.0, 5.0]) == [
        0.375,
        0.0,
        0.625,
        0.125,
        1.0,
    ]


# </test>

#<test>

def test():
    assert rescale_to_unit([1.0, 2.0, 3.0]) == [0.0, 0.5, 1.0]
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([10.0, 20.0, 30.0]) == [0.0, 0.5, 1.0]
    assert rescale_to_unit([1.0, 1.0, 1.0]) == [0.0, 0.0, 0.0]
    assert rescale_to_unit([1.0, -2.0, 3.0, -4.0, 5.0]) == [0.375, 0.0, 0.625, 0.125, 1.0]
#</test>

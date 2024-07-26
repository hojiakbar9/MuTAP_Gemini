[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 These are two examples of codes and their tests.

#<code> 

def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
#</code>

#<test>

def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
#</test>

#<code>

from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
#</code>

#<test>

def test():
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
#</test>

#<original code>



def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [(e + 1) for e in l]


METADATA = {}




#</original code>

generate test in the form of above example tests for the original code:

#<test>
def test():
    assert [/INST]  Sure, I'd be happy to help you write tests for the original code! Here are some examples of tests you could write for the `incr_list` function:
#<test>
def test_empty_list():
    l = []
    result = incr_list(l)

    assert result == []

def test_single_element():

    l = [1]

    result = incr_list(l)

    assert result == [2]

def test_multi_element():

    l = [1, 2, 3, 4, 5]

    result = incr_list(l)

    assert result == [2, 3, 4, 5, 6]

def test_large_list():

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    result = incr_list(l)

    assert result ==
[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

Generate a test function that includes different tests in the form of one line assertion [/INST] These are examples of code and test case function:

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
#</test>  [INST] Based on the examples of function code and their test function, generate test cases for the following function:
#<code>
def triangle_area(a, h):
    
    return a * h / 2.0




#</code>
#<test>
def test():
    assert [/INST]  Certainly! Here are some test cases for the `triangle_area` function:

#<test>

def test():
    assert triangle_area(3, 4) == 9.0
    assert triangle_area(5, 6) == 30.0
    assert triangle_area(2, 3) == 6.0
    assert triangle_area(3, 0) == 0.0
    assert triangle_area(0, 3) == 0.0
#</test>

#<test>

def test():
    x = [1, 2, 3]
    assert triangle_area(x[0], x[1]) == x[0] * x[1] / 2.0
    x = [4, 5, 6]
    assert triangle_area(x[0], x[1]) == x[0] * x[1] / 2.0
    x = [7, 8, 9]
    assert triangle_area(x[0], x[1]) == x[0] * x[1
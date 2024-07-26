def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])

def test():
```python
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





def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])


#</code>

#<test>

def test():
    assert add([1, 2, 3, 4, 5, 6]) == 6
    assert add([1, 2, 3, 4, 5, 7]) == 2
    assert add([1, 3, 5, 7, 9]) == 0
    assert add([2, 4, 6, 8, 10]) == 12
    assert add([1, 4, 7, 10, 13]) == 14
#</test>
```
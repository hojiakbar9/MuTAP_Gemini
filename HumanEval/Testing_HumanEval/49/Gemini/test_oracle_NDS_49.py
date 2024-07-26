def modp(n: int, p: int):
    
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret



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





def modp(n: int, p: int):
    
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret




#</code>

#<test>

def test():
    assert modp(1, 13) == 2
    assert modp(2, 13) == 4
    assert modp(3, 13) == 8
    assert modp(4, 13) == 3
    assert modp(5, 13) == 6
    assert modp(6, 13) == 12
    assert modp(7, 13) == 11
    assert modp(8, 13) == 9
    assert modp(9, 13) == 5
    assert modp(10, 13) == 10
    assert modp(11, 13) == 7
    assert modp(12, 13) == 1
#</test>
```
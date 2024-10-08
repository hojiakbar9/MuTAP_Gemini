from typing import List


def factorize(n: int) -> List[int]:
    
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact



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





from typing import List


def factorize(n: int) -> List[int]:
    
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact




#</code>

#<test>

def test():
    assert factorize(1) == [1]
    assert factorize(2) == [2]
    assert factorize(3) == [3]
    assert factorize(4) == [2, 2]
    assert factorize(5) == [5]
    assert factorize(6) == [2, 3]
    assert factorize(7) == [7]
    assert factorize(8) == [2, 2, 2]
    assert factorize(9) == [3, 3]
    assert factorize(10) == [2, 5]
    assert factorize(12) == [2, 2, 3]
    assert factorize(13) == [13]
    assert factorize(14) == [2, 7]
    assert factorize(15) == [3, 5]
    assert factorize(16) == [2, 2, 2, 2]
    assert factorize(17) == [17]
    assert factorize(18) == [2, 3, 3]
    assert factorize(19) == [19]
    assert factorize(20) == [2, 2, 5]
    assert factorize(21) == [3, 7]
    assert factorize(22) == [2, 11]
    assert factorize(23) == [23]
    assert factorize(24) == [2, 2, 2, 3]
    assert factorize(25) == [5, 5]
    assert factorize(26) == [2, 13]
    assert factorize(27) == [3, 3, 3]
    assert factorize(28) == [2, 2, 7]
    assert factorize(29) == [29]
    assert factorize(30) == [2, 3, 5]
    assert factorize(31) == [31]
    assert factorize(32) == [2, 2, 2, 2, 2]
    assert factorize(33) == [3, 11]
    assert factorize(34) == [2, 17]
    assert factorize(35) == [5, 7]
    assert factorize(36) == [2, 2, 3, 3]
    assert factorize(37) == [37]
    assert factorize(38) == [2, 19]
    assert factorize(39) == [3, 13]
    assert factorize(40) == [2, 2, 2, 5]
    assert factorize(41) == [41]
    assert factorize(42) == [2, 3, 7]
    assert factorize(43) == [43]
    assert factorize(44) == [2, 2, 11]
    assert factorize(45) == [3, 3, 5]
    assert factorize(46) == [2, 23]
    assert factorize(47) == [47]
    assert factorize(48) == [2, 2, 2, 2, 3]
    assert factorize(49) == [7, 7]
    assert factorize(50) == [2, 5, 5]
#</test>
```
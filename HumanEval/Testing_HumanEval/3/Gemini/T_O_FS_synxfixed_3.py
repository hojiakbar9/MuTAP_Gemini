from typing import List


def below_zero(operations: List[int]) -> bool:

    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False


def test():
    assert below_zero([1, 2, -3]) == True
    assert below_zero([1, 2, 3]) == False
    assert below_zero([1, -2, 3]) == True
    assert below_zero([1, 2, 3, -10]) == True
    assert below_zero([1, 2, 3, -2]) == False


# </test>s

#<test>

def test():
    assert below_zero([1, 2, -3]) == True
    assert below_zero([1, 2, 3]) == False
    assert below_zero([1, -2, 3]) == True
    assert below_zero([1, 2, 3, -10]) == True
    assert below_zero([1, 2, 3, -2]) == False
#</test>

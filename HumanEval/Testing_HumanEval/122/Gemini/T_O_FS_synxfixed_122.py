def add_elements(arr, k):
    
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)

#<test>

def test():
    assert add_elements([1, 10, 100, 1000], 3) == 111
    assert add_elements([1, 2, 3], 3) == 6
    assert add_elements([10, 100, 1000], 1) == 10
    assert add_elements([10, 100, 1000], 2) == 110
    assert add_elements([1000, 10, 100], 3) == 110
#</test>

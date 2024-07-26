def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m

#<test>

def test():
    assert max_element([1, 2, 3, 4, 5]) == 5
    assert max_element([5, 4, 3, 2, 1]) == 5
    assert max_element([1, 1, 1, 1, 1]) == 1
    assert max_element([10, 20, 30, 40, 50]) == 50
    assert max_element([-1, -2, -3, -4, -5]) == -1
#</test>

#<test>

def test():
    assert max_element([1, 2, 3, 4, 5]) == 5
    assert max_element([5, 4, 3, 2, 1]) == 5
    assert max_element([1, 1, 1, 1, 1]) == 1
    assert max_element([10, 20, 30, 40, 50]) == 50
    assert max_element([-1, -2, -3, -4, -5]) == -1
#</test>

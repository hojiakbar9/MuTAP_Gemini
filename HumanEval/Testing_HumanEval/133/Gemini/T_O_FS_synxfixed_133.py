def sum_squares(lst):
    
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared

#<test>

def test():
    assert sum_squares([1.1, 2.2, 3.3]) == 18
    assert sum_squares([1.0, 2.0, 3.0, 4.0, 5.0]) == 55
    assert sum_squares([1.0, 1.1, 1.2]) == 4
#</test>

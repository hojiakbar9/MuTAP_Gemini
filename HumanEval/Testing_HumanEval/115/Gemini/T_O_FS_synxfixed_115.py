def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])

#<test>

def test():
    assert max_fill([[1, 2, 3], [4, 5, 6]], 3) == 3
    assert max_fill([[1, 2, 3], [4, 5, 6]], 4) == 2
    assert max_fill([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 5) == 3
#</test>

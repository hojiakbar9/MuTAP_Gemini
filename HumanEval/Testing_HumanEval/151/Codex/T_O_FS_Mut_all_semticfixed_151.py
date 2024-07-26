def double_the_difference(lst):
    
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])




def test():
    assert double_the_difference([0,2,0,2,0]) == 0
    assert double_the_difference([0,2,0,2,0]) == 0
    assert double_the_difference([]) == 0
    assert double_the_difference([0,0,0,0,0]) == 0
    assert double_the_difference([0, 2, 0, 2, 0]) == 0
    assert double_the_difference([0, 2, 4, 0, 2, 4]) == 0
    assert double_the_difference([]) == 0
    assert double_the_difference([0, 0, 0, 0, 0]) == 0
    assert double_the_difference([0, 0, 0, 0, 0, 0]) == 0
    assert double_the_difference([0, 1, 0, 1, 0]) == 2
    assert double_the_difference([-1, -2, -1, -2, -1]) == 0
    assert double_the_difference([0, -1, 0, -1, 0]) == 0
    assert double_the_difference([0,2,0,2,0]) == 0
    assert double_the_difference([0,2,0,2,0]) == 0
    assert double_the_difference([]) == 0
    assert double_the_difference([0,0,0,0,0]) == 0

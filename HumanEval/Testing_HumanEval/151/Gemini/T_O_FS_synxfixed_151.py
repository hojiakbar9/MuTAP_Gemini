def double_the_difference(lst):
    
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])

#<test>

def test():
    assert double_the_difference([1, 2, 3, 4, 5]) == 20
    assert double_the_difference([1, 2, 3, 4, 5.5]) == 20
    assert double_the_difference([1, 2, 3, 4, 6]) == 52
    assert double_the_difference([1, -2, 3, 4, 5]) == 20
    assert double_the_difference([1, 2, 3, 4, 0]) == 20
#</test>

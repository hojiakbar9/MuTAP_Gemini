def largest_smallest_integers(lst):
    
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)

#<test>

def test():
    assert largest_smallest_integers([1, 2, -2, -1]) == (-1, 1)
    assert largest_smallest_integers([1, 2, 3, 4, 5]) == (None, 1)
    assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-1, None)
    assert largest_smallest_integers([]) == (None, None)
#</test>

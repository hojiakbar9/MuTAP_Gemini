def largest_smallest_integers(lst):
    
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)




def test():
    assert largest_smallest_integers([4, -4, 3, -2, -1]) == (-1, 3)
    assert largest_smallest_integers([4, -4, 3, -2, -1, -200]) == (-1, 3)
    assert largest_smallest_integers([4, -4, 3, -2, -1, 200]) == (-1, 3)
    assert largest_smallest_integers([-1, -200, -3, -5]) == (-1, None)
    assert largest_smallest_integers([1, 2, 3, -4, 5]) == (-4, 1)
    assert largest_smallest_integers([1, -2, 3, -4, 5]) == (-2, 1)
    assert largest_smallest_integers([-1, 2,-3, 4, -5]) == (-1, 2)
    assert largest_smallest_integers([4, -4, 3, -2, -1]) == (-1, 3)
    assert largest_smallest_integers([4, -4, 3, -2, -1, -200]) == (-1, 3)
    assert largest_smallest_integers([4, -4, 3, -2, -1, 200]) == (-1, 3)
    assert largest_smallest_integers([-1, -200, -3, -5]) == (-1, None)
    assert largest_smallest_integers([1, 2, 3, -4, 5]) == (-4, 1)
    assert largest_smallest_integers([1, -2, 3, -4, 5]) == (-2, 1)
    assert largest_smallest_integers([1, -2, 3, -4, 5]) == (-2, 1)
    assert largest_smallest_integers([-1, 2, -3, 4, -5]) == (-1, 2)
    assert largest_smallest_integers([1, 2, -3, 4, -5]) == (-3, 1)
    assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-1, None)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-3, -2, -1, 0, 1, 3, -4]) == (-1, 1)

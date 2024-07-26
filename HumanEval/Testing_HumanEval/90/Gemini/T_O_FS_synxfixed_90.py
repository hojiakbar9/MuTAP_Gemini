def next_smallest(lst):
    
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]

#<test>

def test():
    assert next_smallest([1, 2, 3]) == 2
    assert next_smallest([3, 2, 1]) == 2
    assert next_smallest([1, 1, 1]) == None
    assert next_smallest([2, 2, 1, 1, 1, 1]) == 2
#</test>

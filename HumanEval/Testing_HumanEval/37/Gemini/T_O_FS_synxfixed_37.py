def sort_even(l: list):
    
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans

#<test>

def test():
    assert sort_even([1, 2, 3, 4, 5, 6]) == [2, 1, 4, 3, 6, 5]
    assert sort_even([1, 3, 2, 4, 5]) == [2, 1, 4, 3, 5]
    assert sort_even([1, 2, 3, 4]) == [2, 1, 4, 3]
    assert sort_even([1, 2, 3]) == [2, 1, 3]
#</test>

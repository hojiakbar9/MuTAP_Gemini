def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]

#<test>

def test():
    assert pluck([2, 4, 6, 8]) == [2, 0]
    assert pluck([1, 3, 5, 7]) == []
    assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [2, 0]
    assert pluck([3, 7, 9, 1, 2, 10]) == [2, 4]
    assert pluck([1, 5, 9, 13, 17, 21]) == []
#</test>

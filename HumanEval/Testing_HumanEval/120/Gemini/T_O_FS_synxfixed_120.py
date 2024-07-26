def maximum(arr, k):
    
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans

#<test>

def test():
    assert maximum([1, 2, 3, 4, 5], 2) == [4, 5]
    assert maximum([1, 2, 3, 4, 5], 0) == []
    assert maximum([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
#</test>

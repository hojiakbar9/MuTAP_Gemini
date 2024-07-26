def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])

#<test>

def test():
    assert add([1, 2, 3, 4, 5, 6]) == 6
    assert add([1, 2, 3, 4, 5, 7]) == 2
    assert add([1, 3, 5, 7, 9]) == 0
    assert add([2, 4, 6, 8, 10]) == 12
    assert add([1, 4, 7, 10, 13]) == 14
#</test>

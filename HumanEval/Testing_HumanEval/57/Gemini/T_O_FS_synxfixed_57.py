def monotonic(l: list):
    
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False

#<test>

def test():
    assert monotonic([1, 2, 3]) == True
    assert monotonic([3, 2, 1]) == True
    assert monotonic([1, 2, 2]) == True
    assert monotonic([1, 1, 2]) == True
    assert monotonic([1, 1, 1]) == True
    assert monotonic([1, 2, 1]) == False
    assert monotonic([1, 2, 1, 1]) == False
#</test>

def below_threshold(l: list, t: int):
    
    for e in l:
        if e >= t:
            return False
    return True

#<test>

def test():
    assert below_threshold([1, 2, 3], 4) == True
    assert below_threshold([1, 2, 4], 4) == False
    assert below_threshold([1, 2, 3, 4], 4) == False
    assert below_threshold([1, 2, 3], 3) == True
    assert below_threshold([1, 2, 3], 2) == False
#</test>

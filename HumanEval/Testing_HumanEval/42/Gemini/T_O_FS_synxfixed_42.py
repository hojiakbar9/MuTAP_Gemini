def incr_list(l: list):
    
    return [(e + 1) for e in l]

#<test>

def test():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([0, 1, 2]) == [1, 2, 3]
    assert incr_list([10, 12, 14]) == [11, 13, 15]
#</test>

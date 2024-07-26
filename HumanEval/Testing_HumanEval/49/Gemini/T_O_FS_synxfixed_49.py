def modp(n: int, p: int):
    
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret

#<test>

def test():
    assert modp(1, 13) == 2
    assert modp(2, 13) == 4
    assert modp(3, 13) == 8
    assert modp(4, 13) == 3
    assert modp(5, 13) == 6
    assert modp(6, 13) == 12
    assert modp(7, 13) == 11
    assert modp(8, 13) == 9
    assert modp(9, 13) == 5
    assert modp(10, 13) == 10
    assert modp(11, 13) == 7
    assert modp(12, 13) == 1
#</test>

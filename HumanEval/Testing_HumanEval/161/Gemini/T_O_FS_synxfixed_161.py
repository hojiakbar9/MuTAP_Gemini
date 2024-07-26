def solve(s):
    
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s

#<test>

def test():
    assert solve("a1b2c3d4") == "A1B2C3D4"
    assert solve("12345678") == "87654321"
    assert solve("abcde") == "ABCDE"
    assert solve("123abC") == "123AbC"
    assert solve("123") == "321"
#</test>

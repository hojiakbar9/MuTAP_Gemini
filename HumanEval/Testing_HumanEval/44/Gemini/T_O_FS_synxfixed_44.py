def change_base(x: int, base: int):
    
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret

#<test>

def test():
    assert change_base(10, 2) == "1010"
    assert change_base(10, 8) == "12"
    assert change_base(10, 16) == "A"
#</test>

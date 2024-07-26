def multiply(a, b):
    
    return abs(a % 10) * abs(b % 10)

#<test>

def test():
    assert multiply(123, 456) == 18
    assert multiply(999, 111) == 9
    assert multiply(-123, 456) == 18
    assert multiply(123, -456) == 18
    assert multiply(0, 100) == 0
#</test>

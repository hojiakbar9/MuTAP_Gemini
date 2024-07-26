def simplify(x, n):
    
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False

#<test>

def test():
    assert simplify("1/2", "2/3") == True
    assert simplify("1/2", "1/3") == False
    assert simplify("1/2", "1/2") == True
    assert simplify("2/5", "3/4") == False
    assert simplify("6/2", "1/3") == True
#</test>

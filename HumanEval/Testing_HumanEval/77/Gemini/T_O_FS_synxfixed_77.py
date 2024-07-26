def iscube(a):
    
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a

#<test>

def test():
    assert iscube(27) == True
    assert iscube(8) == True
    assert iscube(125) == True
    assert iscube(1) == True
    assert iscube(0) == True
    assert iscube(-8) == True
    assert iscube(2) == False
    assert iscube(10) == False
#</test>

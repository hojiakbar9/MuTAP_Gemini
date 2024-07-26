def choose_num(x, y):
    
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

#<test>

def test():
    assert choose_num(5, 8) == 8
    assert choose_num(3, 3) == -1
    assert choose_num(7, 5) == 4
    assert choose_num(5, 4) == -1
#</test>

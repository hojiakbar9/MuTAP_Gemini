def add(x: int, y: int):
    
    return x + y

#<test>

def test():
    assert add(2, 3) == 5
    assert add(10, 5) == 15
    assert add(-1, 2) == 1
#</test>

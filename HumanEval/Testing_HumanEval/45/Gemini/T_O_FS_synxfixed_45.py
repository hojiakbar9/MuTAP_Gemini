def triangle_area(a, h):
    
    return a * h / 2.0

#<test>

def test():
    assert triangle_area(3, 4) == 6.0
    assert triangle_area(5, 8) == 20.0
#</test>

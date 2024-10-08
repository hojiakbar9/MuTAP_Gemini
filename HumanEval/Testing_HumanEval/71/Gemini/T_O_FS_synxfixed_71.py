def triangle_area(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area

#<test>

def test():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(5, 12, 13) == 30.00
    assert triangle_area(10, 10, 20) == -1
    assert triangle_area(1, 2, 3) == -1 
#</test>

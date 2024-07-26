def derivative(xs: list):
    
    return [(i * x) for i, x in enumerate(xs)][1:]

#<test>

def test():
    assert derivative([1, 2, 3, 4, 5]) == [2, 6, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
#</test>

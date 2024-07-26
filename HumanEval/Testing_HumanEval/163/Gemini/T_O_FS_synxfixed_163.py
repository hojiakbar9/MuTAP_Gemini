def generate_integers(a, b):
    
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

#<test>

def test():
    assert generate_integers(1, 10) == [2, 4, 6, 8]
    assert generate_integers(7, 3) == [2, 4, 6, 8]
    assert generate_integers(1, 2) == [2]
    assert generate_integers(8, 8) == [2, 4, 6, 8]
    assert generate_integers(10, 2) == [2, 4, 6, 8]
#</test>

def x_or_y(n, x, y):
    
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x

#<test>

def test():
    assert x_or_y(1, 'x', 'y') == 'y'
    assert x_or_y(2, 'x', 'y') == 'x'
    assert x_or_y(3, 'x', 'y') == 'x'
    assert x_or_y(4, 'x', 'y') == 'y'
    assert x_or_y(7, 'x', 'y') == 'x'
#</test>

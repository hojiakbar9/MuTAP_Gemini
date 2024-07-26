def is_simple_power(x, n):
    
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x)

#<test>

def test():
    assert is_simple_power(8, 2) == True
    assert is_simple_power(16, 2) == True
    assert is_simple_power(10, 2) == False
    assert is_simple_power(1, 2) == True
    assert is_simple_power(27, 3) == True
#</test>

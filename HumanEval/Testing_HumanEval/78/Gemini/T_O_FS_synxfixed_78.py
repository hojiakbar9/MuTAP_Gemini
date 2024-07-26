def hex_key(num):
    
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total

#<test>

def test():
    assert hex_key('2357BD') == 6
    assert hex_key('A23456') == 3
    assert hex_key('123456') == 1
#</test>

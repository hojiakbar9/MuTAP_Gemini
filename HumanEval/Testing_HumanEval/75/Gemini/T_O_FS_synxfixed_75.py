def is_multiply_prime(a):
    
    def is_prime(n):
        for j in range(2,n):
            if n%j == 0:
                return False
        return True




    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False

#<test>

def test():
    assert is_multiply_prime(210) == True
    assert is_multiply_prime(17) == False
    assert is_multiply_prime(100) == True
    assert is_multiply_prime(15) == True
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(29) == False
    assert is_multiply_prime(999) == True
#</test>

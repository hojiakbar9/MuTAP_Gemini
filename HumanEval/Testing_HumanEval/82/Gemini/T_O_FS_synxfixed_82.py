def prime_length(string):
    
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

#<test>

def test():
    assert prime_length("a") == False
    assert prime_length("abc") == True
    assert prime_length("abcdef") == False
    assert prime_length("12345") == True
    assert prime_length("123456") == False
#</test>

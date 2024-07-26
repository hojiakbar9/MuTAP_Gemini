def cycpattern_check(a , b):
    
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False

#<test>

def test():
    assert cycpattern_check("abcabcabc" , "abc") == True
    assert cycpattern_check("abcabc" , "abc") == True
    assert cycpattern_check("abcabc" , "ab") == True
    assert cycpattern_check("abcabc" , "ac") == False
    assert cycpattern_check("abcabcabc" , "abcabc") == True
    assert cycpattern_check("abcabcabc" , "abcabcd") == False
#</test>

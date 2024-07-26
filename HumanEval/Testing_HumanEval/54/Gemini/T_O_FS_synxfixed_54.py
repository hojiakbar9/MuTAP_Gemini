def same_chars(s0: str, s1: str):
    
    return set(s0) == set(s1)

#<test>

def test():
    assert same_chars("abc", "cab") == True
    assert same_chars("abc", "abb") == False
    assert same_chars("a", "a") == True
    assert same_chars("ab", "") == False
    assert same_chars("", "") == True
#</test>

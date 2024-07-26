def reverse_delete(s,c):
    
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)

#<test>

def test():
    assert reverse_delete("racecar","a") == ("rcecr",True)
    assert reverse_delete("abcabc","abc") == ("",True)
    assert reverse_delete("abcabc","b") == ("acac",False)
#</test>

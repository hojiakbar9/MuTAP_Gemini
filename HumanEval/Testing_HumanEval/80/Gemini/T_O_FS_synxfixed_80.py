def is_happy(s):
    
    if len(s) < 3:
      return False

    for i in range(len(s) - 2):
      
      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
        return False
    return True

#<test>

def test():
    assert is_happy("abc") == True
    assert is_happy("abca") == False
    assert is_happy("aabb") == False
    assert is_happy("ab") == False
    assert is_happy("abcc") == False
#</test>

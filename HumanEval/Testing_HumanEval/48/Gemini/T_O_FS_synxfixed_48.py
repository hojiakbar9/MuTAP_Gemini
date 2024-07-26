def is_palindrome(text: str):
    
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

#<test>

def test():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("rotor") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False
#</test>

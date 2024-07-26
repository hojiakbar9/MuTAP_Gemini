def is_palindrome(string: str) -> bool:

    return string == string[::-1]


def make_palindrome(string: str) -> str:

    if not string:
        return ""

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]


# <test>


def test():
    assert is_palindrome("racecar") == True
    assert is_palindrome("noon") == True
    assert is_palindrome("kayak") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert make_palindrome("abc") == "abccba"
    assert make_palindrome("racecar") == "racecar"
    assert make_palindrome("ab") == "abab"
    assert make_palindrome("a") == "a"
    assert make_palindrome("") == ""


# </test>

#<test>

def test():
    assert is_palindrome("racecar") == True
    assert is_palindrome("noon") == True
    assert is_palindrome("kayak") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert make_palindrome("abc") == "abccba"
    assert make_palindrome("racecar") == "racecar"
    assert make_palindrome("ab") == "abab"
    assert make_palindrome("a") == "a"
    assert make_palindrome("") == ""
#</test>

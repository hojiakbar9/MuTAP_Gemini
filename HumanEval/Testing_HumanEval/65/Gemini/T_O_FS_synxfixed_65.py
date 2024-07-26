def circular_shift(x, shift):
    
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

#<test>

def test():
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift(12345, 5) == "54321"
    assert circular_shift(12345, 10) == "54321"
    assert circular_shift(12345, 0) == "12345"
    assert circular_shift(12345, 1) == "51234"
#</test>

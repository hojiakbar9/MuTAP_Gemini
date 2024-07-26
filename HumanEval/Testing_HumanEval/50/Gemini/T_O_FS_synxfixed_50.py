def encode_shift(s: str):
    
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

#<test>

def test():
    assert encode_shift("abc") == "fgj"
    assert encode_shift("xyz") == "cde"
    assert decode_shift("fgj") == "abc"
    assert decode_shift("cde") == "xyz"
#</test>

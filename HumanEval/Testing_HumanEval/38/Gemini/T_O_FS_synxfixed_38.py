def encode_cyclic(s: str):
    
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    
    return encode_cyclic(encode_cyclic(s))

#<test>

def test():
    assert encode_cyclic("abc") == "bca"
    assert encode_cyclic("abcd") == "bcd"
    assert encode_cyclic("abcde") == "bcdea"
    assert encode_cyclic("abcdef") == "bcdefa"
    assert encode_cyclic("abcdefg") == "bcdefga"
    assert decode_cyclic("bca") == "abc"
    assert decode_cyclic("bcd") == "abcd"
    assert decode_cyclic("bcdea") == "abcde"
    assert decode_cyclic("bcdefa") == "abcdef"
    assert decode_cyclic("bcdefga") == "abcdefg"
#</test>

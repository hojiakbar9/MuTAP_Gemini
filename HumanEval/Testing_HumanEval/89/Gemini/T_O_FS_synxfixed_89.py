def encrypt(s):
    
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out

#<test>

def test():
    assert encrypt("abc") == "cde"
    assert encrypt("xyz") == "zab"
    assert encrypt("123abc") == "123cde"
    assert encrypt("The quick brown fox jumps over the lazy dog") == "Vjg jvtvm dypv jtfn qbt jt qpx lzt hp"
#</test>

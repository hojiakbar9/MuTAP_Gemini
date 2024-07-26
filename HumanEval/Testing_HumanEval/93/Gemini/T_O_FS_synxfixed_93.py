def encode(message):
    
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])

#<test>

def test():
    assert encode("hello") == "hOlLe"
    assert encode("HOW are you?") == "hOw ArE yOu?"
    assert encode("This is a test!") == "tHiS iS c tEsT!"
#</test>

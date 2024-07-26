def string_to_md5(text):
    
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

#<test>

def test():
    assert string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert string_to_md5("") == None
#</test>

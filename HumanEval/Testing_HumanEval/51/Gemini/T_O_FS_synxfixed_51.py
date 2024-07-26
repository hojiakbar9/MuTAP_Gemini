def remove_vowels(text):
    
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])

#<test>

def test():
    assert remove_vowels("This is a test!") == "Ths s  tst!"
    assert remove_vowels("AEIOU") == ""
    assert remove_vowels("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"
    assert remove_vowels("1234567890") == "1234567890"
#</test>

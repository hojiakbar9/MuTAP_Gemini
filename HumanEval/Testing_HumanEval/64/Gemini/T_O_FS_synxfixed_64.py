def vowels_count(s):
    
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels

#<test>

def test():
    assert vowels_count("hello") == 2
    assert vowels_count("world") == 1
    assert vowels_count("aeiouAEIOU") == 10
    assert vowels_count("why") == 2
    assert vowels_count("Why") == 2
#</test>

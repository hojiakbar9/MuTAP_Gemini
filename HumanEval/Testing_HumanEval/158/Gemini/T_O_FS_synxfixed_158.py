def find_max(words):
   
    return sorted(words, key = lambda x: (-len(set(x)), x))[0]

#<test>

def test():
    assert find_max(["this", "is", "a", "test"]) == "test"
    assert find_max(["hello", "world"]) == "world"
    assert find_max(["aa", "bb", "cc"]) == "aa"
    assert find_max(["a", "b", "c"]) == "a"
#</test>

def select_words(s, n):
    
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n:
            result.append(word)
    return result

#<test>

def test():
    assert select_words("The quick brown rabbit jumps over the lazy fox", 3) == ['quick', 'brown', 'rabbit', 'jumps']
    assert select_words("This is a test sentence", 2) == ['This', 'test']
    assert select_words("This is a test sentence", 4) == []
#</test>

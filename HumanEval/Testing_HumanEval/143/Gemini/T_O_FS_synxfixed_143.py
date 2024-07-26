def words_in_sentence(sentence):
    
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word)%i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)

#<test>

def test():
    assert words_in_sentence("This is a test sentence") == "This is a test sentence"
    assert words_in_sentence("This is a test sentence with many words") == "This is a test sentence with many words"
    assert words_in_sentence("The quick brown fox jumps over the lazy dog") == "The quick brown fox jumps over the lazy dog"
    assert words_in_sentence("The quick brown fox jumps over the lazy dog and many more words") == "The quick brown fox jumps over the lazy dog and more"
    assert words_in_sentence("I am a happy man") == "I am a happy man"
    assert words_in_sentence("I am a happy man and I am very happy") == "I am a happy man and I very"
    assert words_in_sentence("I am a happy man and I am very happy") == "I am a happy man and I very"
#</test>

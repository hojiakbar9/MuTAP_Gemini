def is_bored(S):
    
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)

#<test>

def test():
    assert is_bored("I am bored. I am so bored. I am really bored") == 3
    assert is_bored("I am bored. I am not bored.") == 1
    assert is_bored("I am bored. Am I bored?") == 1
    assert is_bored("I am not bored.  I am happy") == 0
    assert is_bored("") == 0
    assert is_bored("I am  bored") == 1
    assert is_bored("I am not bored.  I am happy. I am not bored. I am bored.") == 2
#</test>

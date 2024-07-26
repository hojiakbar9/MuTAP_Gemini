def is_bored(S):

    import re

    sentences = re.split(r"[.?!]\s*", S)
    return sum(sentence[0:2] == "I " for sentence in sentences)


# <test>


def test():
    assert is_bored("I am bored. I am tired. I want to go home.") == 3
    assert is_bored("I am not bored. I like my job. I am happy.") == 1
    assert is_bored("I am bored. I am not bored.") == 2

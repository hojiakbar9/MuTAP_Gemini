def count_distinct_characters(string: str) -> int:

    return len(set(string.lower()))


# <test>


def test():
    assert count_distinct_characters("abc") == 3
    assert count_distinct_characters("aba") == 2
    assert count_distinct_characters("aAa") == 1
    assert count_distinct_characters("aA1") == 3
    assert count_distinct_characters("123") == 3
    assert count_distinct_characters("") == 0


# </test>

#<test>

def test():
    assert count_distinct_characters("abc") == 3
    assert count_distinct_characters("aba") == 2
    assert count_distinct_characters("aAa") == 1
    assert count_distinct_characters("aA1") == 3
    assert count_distinct_characters("123") == 3
    assert count_distinct_characters("") == 0
#</test>

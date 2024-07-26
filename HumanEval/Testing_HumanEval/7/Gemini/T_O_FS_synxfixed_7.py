from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:

    return [x for x in strings if substring in x]


def test():
    assert filter_by_substring(["hello", "world", "apple", "banana"], "o") == [
        "hello",
        "world",
        "apple",
    ]
    assert filter_by_substring(["hello", "world", "apple", "banana"], "an") == [
        "banana"
    ]
    assert filter_by_substring(["hello", "world", "apple", "banana"], "x") == []


# </test>

#<test>

def test():
    assert filter_by_substring(["hello", "world", "apple", "banana"], "o") == ["hello", "world", "apple"]
    assert filter_by_substring(["hello", "world", "apple", "banana"], "an") == ["banana"]
    assert filter_by_substring(["hello", "world", "apple", "banana"], "x") == []
#</test>

from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:

    return [x for x in strings if x.startswith(prefix)]


# <test>


def test():
    assert filter_by_prefix(["hello", "world", "hell", "help", "he"], "hel") == [
        "hello",
        "hell",
        "help",
        "he",
    ]
    assert filter_by_prefix(["hello", "world", "hell", "help", "he"], "wor") == [
        "world"
    ]
    assert filter_by_prefix(["hello", "world", "hell", "help", "he"], "h") == [
        "hello",
        "world",
        "hell",
        "help",
        "he",
    ]
    assert filter_by_prefix(["hello", "world", "hell", "help", "he"], "hellll") == []
    assert filter_by_prefix([], "hellll") == []


# </test>

#<test>

def test():
    assert filter_by_prefix(["hello", "world", "hell", "help", "he"], "hel") == ["hello", "hell", "help", "he"]
    assert filter_by_prefix(["hello", "world", "hell", "help", "he"], "wor") == ["world"]
    assert filter_by_prefix(["hello", "world", "hell", "help", "he"], "h") == ["hello", "world", "hell", "help", "he"]
    assert filter_by_prefix(["hello", "world", "hell", "help", "he"], "hellll") == []
    assert filter_by_prefix([], "hellll") == []
#</test>

from typing import List


def all_prefixes(string: str) -> List[str]:

    result = []

    for i in range(len(string)):
        result.append(string[: i + 1])
    return result


# <test>


def test():
    assert all_prefixes("test") == ["t", "te", "tes", "test"]
    assert all_prefixes("ab") == ["a", "ab"]
    assert all_prefixes("a") == ["a"]
    assert all_prefixes("") == []


# </test>

#<test>

def test():
    assert all_prefixes("test") == ["t", "te", "tes", "test"]
    assert all_prefixes("ab") == ["a", "ab"]
    assert all_prefixes("a") == ["a"]
    assert all_prefixes("") == []
#</test>

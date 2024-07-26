def how_many_times(string: str, substring: str) -> int:

    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i : i + len(substring)] == substring:
            times += 1

    return times


# <test>


def test():
    assert how_many_times("ababa", "aba") == 2
    assert how_many_times("ababa", "a") == 3
    assert how_many_times("ababa", "b") == 2
    assert how_many_times("ababa", "aba") == 2
    assert how_many_times("ababa", "ababa") == 1


# </test>

#<test>

def test():
    assert how_many_times("ababa", "aba") == 2
    assert how_many_times("ababa", "a") == 3
    assert how_many_times("ababa", "b") == 2
    assert how_many_times("ababa", "aba") == 2
    assert how_many_times("ababa", "ababa") == 1
#</test>

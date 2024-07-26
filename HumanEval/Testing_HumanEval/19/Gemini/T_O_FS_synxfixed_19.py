from typing import List


def sort_numbers(numbers: str) -> str:

    value_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    return " ".join(
        sorted([x for x in numbers.split(" ") if x], key=lambda x: value_map[x])
    )


# <test>


def test():
    assert sort_numbers("one four two three") == "one two three four"
    assert (
        sort_numbers("zero one two three four five six seven eight nine")
        == "zero one two three four five six seven eight nine"
    )
    assert sort_numbers("two one three") == "one two three"
    assert sort_numbers("eight nine zero") == "zero eight nine"


# </test>

# <test>

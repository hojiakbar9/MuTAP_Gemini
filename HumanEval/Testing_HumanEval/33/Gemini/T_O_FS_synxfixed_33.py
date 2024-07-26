def sort_third(l: list):

    l = list(l)
    l[::3] = sorted(l[::3])
    return l


# <test>


def test():
    assert sort_third([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert sort_third([1, 5, 3, 4, 2, 6]) == [1, 2, 3, 4, 5, 6]
    assert sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
    ]
    assert sort_third([1, 5, 3, 4, 2, 6, 7, 8, 9, 10, 11, 12]) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
    ]


# </test>

#<test>

def test():
    assert sort_third([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert sort_third([1, 5, 3, 4, 2, 6]) == [1, 2, 3, 4, 5, 6]
    assert sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert sort_third([1, 5, 3, 4, 2, 6, 7, 8, 9, 10, 11, 12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#</test>

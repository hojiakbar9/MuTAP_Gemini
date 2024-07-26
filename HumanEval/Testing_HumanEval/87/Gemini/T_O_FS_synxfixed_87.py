def get_row(lst, x):
    
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])

#<test>

def test():
    assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [(1, 1)]
    assert get_row([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 12) == [(2, 3)]
    assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [(0, 0)]
    assert get_row([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 1) == [(0, 0)]
    assert get_row([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 10) == [(2, 1)]
#</test>

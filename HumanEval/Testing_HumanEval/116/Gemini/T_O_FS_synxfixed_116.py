def sort_array(arr):
    
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))

#<test>

def test():
    assert sort_array([1, 7, 3, 11, 2, 9]) == [1, 2, 3, 11, 7, 9]
    assert sort_array([4, 1, 2, 8, 5, 0]) == [0, 1, 2, 5, 8, 4]
    assert sort_array([3, 7, 8, 5, 12]) == [3, 5, 7, 8, 12]
#</test>

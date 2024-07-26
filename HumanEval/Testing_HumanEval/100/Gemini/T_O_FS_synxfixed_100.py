def make_a_pile(n):
    
    return [n + 2*i for i in range(n)]

#<test>

def test():
    assert make_a_pile(1) == [1, 3]
    assert make_a_pile(2) == [2, 4, 6]
    assert make_a_pile(3) == [3, 5, 7, 9]
#</test>

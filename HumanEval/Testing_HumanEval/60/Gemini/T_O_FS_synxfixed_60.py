def sum_to_n(n: int):
    
    return sum(range(n + 1))

#<test>

def test():
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(1) == 1
#</test>

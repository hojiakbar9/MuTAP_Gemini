def pairs_sum_to_zero(l):
    
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

#<test>

def test():
    assert pairs_sum_to_zero([1, 2, -2, 4]) == True
    assert pairs_sum_to_zero([1, 2, 3, 4]) == False
    assert pairs_sum_to_zero([1, 2, -3, 4]) == False
    assert pairs_sum_to_zero([-1, -2, 1, 2]) == True
#</test>

def triples_sum_to_zero(l: list):
    
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

#<test>

def test():
    assert triples_sum_to_zero([1, 2, -3]) == True
    assert triples_sum_to_zero([1, 2, 3]) == False
    assert triples_sum_to_zero([1, 0, -1, 2, -2]) == True
    assert triples_sum_to_zero([1, 1, 1, 1, 1, 1]) == False
    assert triples_sum_to_zero([0, 0, 0]) == True
#</test>

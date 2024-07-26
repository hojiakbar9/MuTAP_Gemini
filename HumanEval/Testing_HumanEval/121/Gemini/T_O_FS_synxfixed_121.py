def solution(lst):
    
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])

#<test>

def test():
    assert solution([1, 2, 3, 4, 5]) == 6
    assert solution([1, 3, 5, 7, 9]) == 16
    assert solution([2, 4, 6, 8, 10]) == 0
#</test>

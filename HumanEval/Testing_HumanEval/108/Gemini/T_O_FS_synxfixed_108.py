def count_nums(arr):
    
    def digits_sum(n):
        neg = 1
        if n < 0: 
            n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))

#<test>

def test():
    assert count_nums([2, -3, 1, 0, 5, -10]) == 4
    assert count_nums([11, 12, 13, 14]) == 4
    assert count_nums([100, -100, 10, -10]) == 2
    assert count_nums([11, 12, -13, 14]) == 3
#</test>

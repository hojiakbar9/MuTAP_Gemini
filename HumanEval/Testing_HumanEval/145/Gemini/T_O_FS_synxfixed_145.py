def order_by_points(nums):
    
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)

#<test>

def test():
    assert order_by_points([10, -11, 2, 3, 4]) == [-11, 2, 3, 4, 10]
    assert order_by_points([100, 101, -100, -101]) == [-101, -100, 100, 101]
    assert order_by_points([1, 11, 22, 33, 44]) == [1, 11, 22, 33, 44]
#</test>

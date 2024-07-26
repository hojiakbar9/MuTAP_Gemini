def rounded_avg(n, m):
    
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))

#<test>

def test():
    assert rounded_avg(1, 5) == "0b10"
    assert rounded_avg(3, 8) == "0b11"
    assert rounded_avg(2, 7) == "0b10"
    assert rounded_avg(1, 10) == "0b10"
    assert rounded_avg(10, 1) == -1
#</test>

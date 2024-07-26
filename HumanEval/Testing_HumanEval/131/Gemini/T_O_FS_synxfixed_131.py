def digits(n):
    
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit%2 == 1:
            product= product*int_digit
            odd_count+=1
    if odd_count ==0:
        return 0
    else:
        return product

#<test>

def test():
    assert digits(12345) == 15
    assert digits(2468) == 0
    assert digits(13579) == 945
    assert digits(1) == 1
#</test>

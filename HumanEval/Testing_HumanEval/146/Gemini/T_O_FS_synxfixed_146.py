def specialFilter(nums):
    
    
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
        
    return count

#<test>

def test():
    assert specialFilter([11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 23, 25, 27, 29]) == 6
    assert specialFilter([10, 12, 21, 30, 41, 52, 63, 74, 85, 96]) == 3
    assert specialFilter([21, 33, 45, 67, 89, 101, 123, 145, 167, 189]) == 10
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
#</test>

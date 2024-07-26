def even_odd_count(num):
    
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

#<test>

def test():
    assert even_odd_count(123456) == (3, 3)
    assert even_odd_count(1111) == (0, 4)
    assert even_odd_count(222222) == (6, 0)
    assert even_odd_count(-123456) == (3, 3)
    assert even_odd_count(0) == (1, 0)
#</test>

def odd_count(lst):
    
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res

#<test>

def test():
    assert odd_count(['12345', '67890', '13579']) == ['the number of odd elements is 3 in the string.', 'the number of odd elements is 2 in the string.', 'the number of odd elements is 5 in the string.']
#</test>

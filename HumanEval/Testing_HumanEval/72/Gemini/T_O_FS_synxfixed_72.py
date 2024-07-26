def will_it_fly(q,w):
   
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True

#<test>

def test():
    assert will_it_fly([1,2,3,3,2,1], 10) == True
    assert will_it_fly([1,2,2,2,2,1], 10) == True
    assert will_it_fly([1,1,1,1,1,1], 1) == False
    assert will_it_fly([1,2,3,4,5,6], 15) == False
    assert will_it_fly([1,2,3,3,2,1], 8) == True
#</test>

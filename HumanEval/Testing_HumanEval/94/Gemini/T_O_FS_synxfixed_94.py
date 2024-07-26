def skjkasdkd(lst):
    
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result

#<test>

def test():
    assert skjkasdkd([1,2,3,4,5,6,7,8,9]) == 10
    assert skjkasdkd([1,2,3,4,5,6,7,8,9, 11]) == 2
    assert skjkasdkd([17, 19, 23, 29, 31]) == 13
#</test>

def solve(N):
    
    return bin(sum(int(i) for i in str(N)))[2:]

#<test>

def test():
    assert solve(123) == "1000"
    assert solve(111) == "11"
    assert solve(0) == "0"
#</test>

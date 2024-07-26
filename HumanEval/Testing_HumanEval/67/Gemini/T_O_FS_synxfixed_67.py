def fruit_distribution(s,n):
    
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)

#<test>

def test():
    assert fruit_distribution("5 3 1 2", 10) == 0
    assert fruit_distribution("1 2 3 4 5", 10) == -15
    assert fruit_distribution("3", 3) == 0
    assert fruit_distribution("3 5 1", 7) == -1
    assert fruit_distribution("", 10) == 10
#</test>

def eat(number, need, remaining):
    
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]

#<test>

def test():
    assert eat(1, 2, 3) == [3, 1]
    assert eat(1, 2, 1) == [2, 0]
    assert eat(1, 2, 5) == [3, 3]
    assert eat(1, 10, 1) == [2, 0]
#</test>

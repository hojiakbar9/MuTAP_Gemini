def count_upper(s):
    
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count

#<test>

def test():
    assert count_upper("ABCDE") == 2
    assert count_upper("aBcDe") == 1
    assert count_upper("12345") == 0
    assert count_upper("AEIOU") == 3
#</test>

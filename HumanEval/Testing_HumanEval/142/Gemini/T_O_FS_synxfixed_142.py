def sum_squares(lst):
    
    result =[]
    for i in range(len(lst)):
        if i %3 == 0:
            result.append(lst[i]**2)
        elif i % 4 == 0 and i%3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    return sum(result)

#<test>

def test():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 100
    assert sum_squares([1, 2, 3, 4, 5]) == 32
    assert sum_squares([1, 2]) == 3
#</test>

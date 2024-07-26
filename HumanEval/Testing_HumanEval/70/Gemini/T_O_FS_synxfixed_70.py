def strange_sort_list(lst):
    
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res

#<test>

def test():
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert strange_sort_list([5, 4, 3, 2, 1]) == [5, 1, 4, 2, 3]
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
#</test>

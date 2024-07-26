def sorted_list_sum(lst):
    
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)

#<test>

def test():
    assert sorted_list_sum(['a', 'bb', 'ccc', 'dddd']) == ['bb', 'dddd']
    assert sorted_list_sum(['a', 'bb', 'ccc', 'dddd', 'eeeee']) == ['bb', 'dddd']
    assert sorted_list_sum(['ccc', 'dddd', 'a', 'bb']) == ['bb', 'dddd']
    assert sorted_list_sum(['a']) == []
#</test>

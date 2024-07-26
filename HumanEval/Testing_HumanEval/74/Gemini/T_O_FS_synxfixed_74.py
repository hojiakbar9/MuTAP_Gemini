def total_match(lst1, lst2):
   
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2

#<test>

def test():
    assert total_match(["a", "b", "c"], ["d", "e", "f"]) == ["a", "b", "c"]
    assert total_match(["a", "bc"], ["d", "e"]) == ["d", "e"]
    assert total_match(["a", "bb", "ccc"], ["d", "ee", "fff"]) == ["d", "ee", "fff"]
#</test>

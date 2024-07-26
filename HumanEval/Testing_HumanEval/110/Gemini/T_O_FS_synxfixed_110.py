def exchange(lst1, lst2):
    
    odd = 0
    even = 0
    for i in lst1:
        if i%2 == 1:
            odd += 1
    for i in lst2:
        if i%2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"

#<test>

def test():
    assert exchange([1, 2, 3, 4], [5, 6, 7, 8]) == "YES"
    assert exchange([1, 2, 3, 4], [5, 6, 7, 9]) == "NO"
    assert exchange([1, 3, 5, 7], [2, 4, 6, 8]) == "YES"
    assert exchange([1, 3, 5, 7], [2, 4, 6]) == "YES"
    assert exchange([1, 3, 5, 7], [2, 4]) == "YES"
#</test>

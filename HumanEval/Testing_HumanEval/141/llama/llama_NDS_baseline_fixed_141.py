def file_name_check(file_name):
    
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'


# test case

def test():
    assert file_name_check("example.txt") == "Yes", "File name should be valid"
    assert file_name_check("example. ABC") == "No", "File name should not contain non-alpha characters"
    assert file_name_check("example.txt\0") == "No", "File name should not contain null characters"
    assert file_name_check("example.txt ABC") == "No", "File name should not have illegal extensions"
    assert file_name_check("example.txt ABC") == "No", "File name should not have length > 3"

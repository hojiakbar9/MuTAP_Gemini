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

#<test>

def test():
    assert file_name_check("my.txt") == "Yes"
    assert file_name_check("123.exe") == "No"
    assert file_name_check("a123.dll") == "Yes"
    assert file_name_check("a1234.txt") == "No"
    assert file_name_check("my.doc") == "No"
    assert file_name_check("my") == "No"
    assert file_name_check("123.txt") == "No"
    assert file_name_check("123.123.exe") == "No"
    assert file_name_check(".txt") == "No"
#</test>

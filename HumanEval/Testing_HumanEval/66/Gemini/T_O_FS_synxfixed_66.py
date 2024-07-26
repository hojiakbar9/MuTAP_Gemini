def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

#<test>

def test():
    assert digitSum("a") == 0
    assert digitSum("A") == 65
    assert digitSum("AB") == 130
    assert digitSum("ab") == 0
    assert digitSum("Ab") == 65
#</test>

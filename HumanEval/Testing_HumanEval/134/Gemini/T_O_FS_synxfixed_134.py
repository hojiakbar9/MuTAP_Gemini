def check_if_last_char_is_a_letter(txt):
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

#<test>

def test():
    assert check_if_last_char_is_a_letter("This is a test") == True
    assert check_if_last_char_is_a_letter("This is a test!") == False
    assert check_if_last_char_is_a_letter("This is a test.") == False
    assert check_if_last_char_is_a_letter("This is a test 1") == False
    assert check_if_last_char_is_a_letter("This is a test 12") == False
    assert check_if_last_char_is_a_letter("This is a test1") == False
    assert check_if_last_char_is_a_letter("This is a test 111") == False
    assert check_if_last_char_is_a_letter("This is a test ") == True
    assert check_if_last_char_is_a_letter("This is a test  ") == True
#</test>

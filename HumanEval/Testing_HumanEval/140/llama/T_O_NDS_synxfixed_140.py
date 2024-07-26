
def fix_spaces(text):
   
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        if text[i] == " ":
            end += 1
        else:
            if end - start > 2:
                new_text += "-"+text[i]
            elif end - start > 0:
                new_text += "_"*(end - start)+text[i]
            else:
                new_text += text[i]
            start, end = i+1, i+1
        i+=1
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "_"
    return new_text


# test case
def test():
    
    # Test 1: No spaces
    assert fix_spaces("hello world") == "hello-world"

    # Test 2: Single space
    assert fix_spaces("hello   world") == "hello-world"

    # Test 3: Multiple spaces
    assert fix_spaces("   hello   world") == "hello-world"

    # Test 4: Mix of single and multiple spaces
    assert fix_spaces("hello world   ") == "hello-world"

    # Test 5: Very long string with spaces
    assert fix_spaces("this is a very long string with multiple spaces") == "this-is-a-very-long-string-with-multiple-spaces"

    # Test 6: Uppercase and lowercase
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

#<test>

def test():
    assert fix_spaces("  hello  world  ") == "__hello__world__"
    assert fix_spaces("  hello world  ") == "__hello_world__"
    assert fix_spaces("  hello  world   ") == "__hello__world___"
    assert fix_spaces("hello world") == "hello_world"
    assert fix_spaces(" hello  world ") == "_hello__world_"
    assert fix_spaces("  hello  world ") == "__hello__world_"
    assert fix_spaces(" hello world   ") == "_hello_world___"
    assert fix_spaces(" hello   world   ") == "_hello___world___"
    assert fix_spaces(" hello world") == "_hello_world"
    assert fix_spaces("hello   world") == "hello___world"
#</test>

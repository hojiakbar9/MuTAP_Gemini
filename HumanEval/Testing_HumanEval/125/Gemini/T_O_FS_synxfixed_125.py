def split_words(txt):
    
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])

#<test>

def test():
    assert split_words("This is a test") == ['This', 'is', 'a', 'test']
    assert split_words("This,is,a,test") == ['This', 'is', 'a', 'test']
    assert split_words("test") == 2
#</test>

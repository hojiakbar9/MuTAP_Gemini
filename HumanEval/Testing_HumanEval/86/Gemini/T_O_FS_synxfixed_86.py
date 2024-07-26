def anti_shuffle(s):
    
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])

#<test>

def test():
    assert anti_shuffle("hello world") == "ehllo dlorw"
    assert anti_shuffle("world is round") == "dlorw  is  rndou"
    assert anti_shuffle("python is cool") == "hnoppy  is  cloo"
#</test>

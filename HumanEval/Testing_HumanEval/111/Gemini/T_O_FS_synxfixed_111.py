def histogram(test):
    
    dict1={}
    list1=test.split(" ")
    t=0

    for i in list1:
        if(list1.count(i)>t) and i!='':
            t=list1.count(i)
    if t>0:
        for i in list1:
            if(list1.count(i)==t):
                
                dict1[i]=t
    return dict1

#<test>

def test():
    assert histogram("one one two three four five six one one two three one") == {'one': 5, 'two': 2, 'three': 2}
#</test>

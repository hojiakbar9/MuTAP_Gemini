def compare_one(a, b):
    
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): 
        temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): 
        temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): 
        return None
    return a if float(temp_a) > float(temp_b) else b

#<test>

def test():
    assert compare_one(1, 2) == 2
    assert compare_one(2, 1) == 2
    assert compare_one(1, 1) == None
    assert compare_one('1', '2') == '2'
    assert compare_one('2', '1') == '2'
    assert compare_one('1.0', '1') == None
    assert compare_one('1,0', '1') == None
    assert compare_one(1, '2') == '2'
    assert compare_one('1', 2) == 2
#</test>

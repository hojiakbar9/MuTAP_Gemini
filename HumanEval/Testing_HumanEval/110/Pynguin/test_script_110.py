# Automatically generated by Pynguin.
import script_110 as module_0



def test_case_0():
    bool_0 = True
    set_0 = {bool_0}
    var_0 = module_0.exchange(set_0, set_0)
    assert var_0 == "NO"
    

def test_case_1():
    list_0 = []
    var_0 = module_0.exchange(list_0, list_0)
    assert var_0 == "YES"
    



def test_case_3():
    int_0 = 692
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    bytes_0 = b"\xae"
    var_0 = module_0.exchange(bytes_0, bytes_0)
    assert var_0 == "YES"
   
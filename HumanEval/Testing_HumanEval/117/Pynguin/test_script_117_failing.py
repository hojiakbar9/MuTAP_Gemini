# Automatically generated by Pynguin.
import script_117 as module_0


def test_case_0():
    try:
        tuple_0 = ()
        bytes_0 = None
        var_0 = module_0.select_words(tuple_0, bytes_0)
    except BaseException:
        pass


def test_case_1():
    try:
        bool_0 = True
        str_0 = '$u'
        dict_0 = {bool_0: bool_0, bool_0: bool_0}
        var_0 = module_0.select_words(str_0, dict_0)
        assert var_0 == []
        str_1 = ''
        var_1 = module_0.select_words(str_0, bool_0)
        assert var_1 == ['$u']
        var_2 = module_0.select_words(str_0, str_1)
        assert var_2 == []
        list_0 = [dict_0]
        str_2 = ''
        complex_0 = None
        var_3 = module_0.select_words(str_2, complex_0)
        var_4 = module_0.select_words(list_0, dict_0)
    except BaseException:
        pass

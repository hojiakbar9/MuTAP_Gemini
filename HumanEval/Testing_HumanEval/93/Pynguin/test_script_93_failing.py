# Automatically generated by Pynguin.
import script_93 as module_0


def test_case_0():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0, bool_0}
        var_0 = module_0.encode(set_0)
    except BaseException:
        pass


def test_case_1():
    try:
        bytes_0 = b"@\xa8'\xb7l\xca`"
        var_0 = module_0.encode(bytes_0)
    except BaseException:
        pass


def test_case_2():
    try:
        str_0 = "t)7N%R'^Y,uYCaO|4#"
        var_0 = module_0.encode(str_0)
        assert var_0 == "T)7n%r'^y,WycCq|4#"
        bool_0 = False
        set_0 = {bool_0}
        var_1 = module_0.encode(set_0)
    except BaseException:
        pass

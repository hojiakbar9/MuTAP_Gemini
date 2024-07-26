def flip_case(string: str) -> str:

    return string.swapcase()


# <test>


def test():
    assert flip_case("aBcDeFg") == "AbCdEfG"
    assert flip_case("hELLo") == "HeLlO"
    assert flip_case("wORLd") == "WoRlD"


# </test>

#<test>

def test():
    assert flip_case('aBcDeFg') == 'AbCdEfG'
    assert flip_case('hELLo') == 'HeLlO'
    assert flip_case('wORLd') == 'WoRlD'
#</test>

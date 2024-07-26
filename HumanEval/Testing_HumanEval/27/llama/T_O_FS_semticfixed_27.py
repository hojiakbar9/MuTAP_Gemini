def flip_case(string: str) -> str:
    
    return string.swapcase()




#<test>


def test():
    assert flip_case("") == ""
    assert flip_case("hello") == "HELLO"
    assert flip_case("world") == "WORLD"
    assert flip_case("python") == "PYTHON"
    assert flip_case("HeLlO wOrLd") == "hElLo WoRlD"

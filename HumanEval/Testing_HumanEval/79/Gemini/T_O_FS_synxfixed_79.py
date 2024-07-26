def decimal_to_binary(decimal):
    
    return "db" + bin(decimal)[2:] + "db"

#<test>

def test():
    assert decimal_to_binary(10) == "db1010db"
    assert decimal_to_binary(5) == "db101db"
    assert decimal_to_binary(1) == "db1db"
    assert decimal_to_binary(0) == "db0db"
#</test>

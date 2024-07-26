def do_algebra(operator, operand):
    
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)

#<test>

def test():
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == 5
    assert do_algebra(['*', '/', '+'], [1, 2, 3, 4]) == 7
    assert do_algebra(['-', '+', '*'], [1, 2, 3, 4]) == 11
    assert do_algebra(['+', '*', '/'], [1, 2, 3, 4]) == 2.5
    assert do_algebra(['-', '/', '*'], [1, 2, 3, 4]) == -1.5
#</test>

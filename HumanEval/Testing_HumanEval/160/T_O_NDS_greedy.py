def do_algebra(operator, operand):
    
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)
assert do_algebra(['+', '-', '*', '/'], [1, 2, 3, 4]) == -9

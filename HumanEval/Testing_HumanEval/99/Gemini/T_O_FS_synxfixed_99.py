def closest_integer(value):
    
    from math import floor, ceil

    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res

#<test>

def test():
    assert closest_integer("1.5") == 2
    assert closest_integer("2.5") == 3
    assert closest_integer("1.4") == 1
    assert closest_integer("2.6") == 3
    assert closest_integer("-1.5") == -2
    assert closest_integer("-2.5") == -3
    assert closest_integer("-1.4") == -1
    assert closest_integer("-2.6") == -3
    assert closest_integer("1") == 1
    assert closest_integer("2") == 2
    assert closest_integer("") == 0
    assert closest_integer("1.0") == 1
    assert closest_integer("2.0") == 2
    assert closest_integer("1.00") == 1
    assert closest_integer("2.00") == 2
#</test>

def compare(game,guess):
    
    return [abs(x-y) for x,y in zip(game,guess)]

#<test>

def test():
    assert compare([1, 2, 3], [2, 3, 4]) == [1, 1, 1]
    assert compare([1, 2, 3], [2, 1, 3]) == [1, 1, 0]
    assert compare([1, 2, 3], [1, 1, 1]) == [0, 1, 2]
#</test>

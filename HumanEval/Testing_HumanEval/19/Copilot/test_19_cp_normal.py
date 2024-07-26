from script_19_cp_few_shot import sort_numbers

def test_sort_numbers():
    assert sort_numbers('zero') == 'zero'
    assert sort_numbers('one') == 'one'
    assert sort_numbers('two') == 'two'
    assert sort_numbers('three') == 'three'
    assert sort_numbers('four') == 'four'
    assert sort_numbers('five') == 'five'
    assert sort_numbers('six') == 'six'
    assert sort_numbers('seven') == 'seven'
    assert sort_numbers('eight') == 'eight'
    assert sort_numbers('nine') == 'nine'
    assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('nine eight seven six five four three two one zero') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('four five six seven eight nine zero one two three') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('three two one zero nine eight seven six five four') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('two three four five six seven eight nine zero one') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('one zero nine eight seven six five four three two') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('eight nine zero one two three four five six seven') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('seven six five four three two one zero nine eight') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('six seven eight nine zero one two three four five') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('five four three two one zero nine eight seven six') == 'zero one two three four five six seven eight nine'
   
def move_one_ball(arr):
    
    if len(arr)==0:
      return True
    sorted_array=sorted(arr)
    my_arr=[]
    
    min_value=min(arr)
    min_index=arr.index(min_value)
    my_arr=arr[min_index:]+arr[0:min_index]
    for i in range(len(arr)):
      if my_arr[i]!=sorted_array[i]:
        return False
    return True

#<test>

def test():
    assert move_one_ball([1, 2, 3, 4, 5]) == True
    assert move_one_ball([1, 5, 2, 3, 4]) == True
    assert move_one_ball([1, 5, 2, 4, 3]) == False
    assert move_one_ball([1, 4, 3, 5, 2]) == True
    assert move_one_ball([1, 5, 3, 4, 2]) == False
    assert move_one_ball([1, 5, 2, 3, 4, 6]) == True
    assert move_one_ball([6, 1, 2, 3, 4, 5]) == True
    assert move_one_ball([6, 1, 2, 3, 4, 5]) == True
#</test>

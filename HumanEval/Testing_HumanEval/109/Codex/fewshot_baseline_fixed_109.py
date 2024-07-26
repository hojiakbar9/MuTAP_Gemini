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


def test():
    assert move_one_ball([10, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert move_one_ball([1, 2, 3, 3, 3]) == True

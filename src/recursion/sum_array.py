def sum_array(arr):
    
    if len(arr) == 1:
        return arr[0]

    return arr[0] + sum_array(arr[1:])


assert sum_array([1, 2, 3, 4]) == 10
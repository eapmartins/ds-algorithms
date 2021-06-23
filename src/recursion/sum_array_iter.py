def sum_array_iter(arr):
    result = 0
    
    for i in arr:
        result += i

    return result


assert sum_array_iter([1, 2, 3, 4]) == 10
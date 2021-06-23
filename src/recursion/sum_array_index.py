def sum_array_index(arr, index):
    
    if len(arr) - 1 == index:
        return arr[index]

    return arr[index] + sum_array_index(arr, index + 1)


assert sum_array_index([1, 2, 3, 4], 0) == 10
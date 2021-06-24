def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """

    if arr == [9]:
        return [1, 0]

    if arr[-1] < 9:
        arr[-1] += 1
    else:
        arr = add_one(arr[:-1]) + [0]

    return arr

assert add_one([9, 9, 9]) == [1, 0, 0, 0]
assert add_one([1, 2, 3]) == [1, 2, 4]
assert add_one([1, 2, 3, 9]) == [1, 2, 4, 0]
assert add_one([9]) == [1, 0]
assert add_one([0]) == [1]
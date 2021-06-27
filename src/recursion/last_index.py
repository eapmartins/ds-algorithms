def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    """

    return _last_index_helper(arr, target, len(arr) -1)

def _last_index_helper(arr, target, index):

    if index < 0:
        return -1

    if arr[index] == target:
        return index

    return _last_index_helper(arr, target, index -1)

assert last_index([1, 2, 5, 5, 1, 2, 5, 4], 5) == 6
assert last_index([1, 2, 5, 5, 1, 2, 5, 4], 7) == -1
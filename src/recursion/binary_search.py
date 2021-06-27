def binary_search(arr, target):
    return _binary_search_helper(arr, 0, len(arr) -1, target)

def _binary_search_helper(arr, start_index, end_index, target):

    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2

    if arr[mid_index] == target:
        return mid_index
    elif arr[mid_index] > target:
        return _binary_search_helper(arr, start_index, mid_index -1, target)
    else:
        return _binary_search_helper(arr, mid_index + 1, end_index, target)

assert binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 5) == 5
assert binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 15) == -1
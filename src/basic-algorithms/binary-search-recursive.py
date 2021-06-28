def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using recursion
    
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
         
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    return _binary_search_helper(array, target, 0, len(array) - 1)

def _binary_search_helper(array, target, start_index, end_index):

    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if target == mid_element:
        return mid_index

    if target > mid_element:
        return _binary_search_helper(array, target, mid_element + 1, end_index)

    return _binary_search_helper(array, target, start_index, mid_element - 1)


assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == 1
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15) == -1
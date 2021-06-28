def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    start_index = 0
    end_index = len(array) -1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        mid_element = array[mid_index]

        if target == mid_element:
            return mid_index

        if target < mid_element:
            end_index = mid_index -1
        else:
            start_index = mid_index + 1

    return -1

assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == 1
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15) == -1
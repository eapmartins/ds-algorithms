def deep_reverse(arr):

    if len(arr) < 1:
        return arr

    reversed_items = []

    for item in arr[::-1]:
        if type(item) is list:
            item = deep_reverse(item)

        reversed_items.append(item)
    
    return reversed_items

assert deep_reverse([1, 2, [3, 4, 5], 4, 5]) == [5, 4, [5, 4, 3], 2, 1]
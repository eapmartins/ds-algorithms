def subsets(arr):
    return return_subsets(arr, 0)

def return_subsets(arr, index):
    if index >= len(arr):
        return [[]]

    small_output = return_subsets(arr, index + 1)

    output = list()

    for element in small_output:
        output.append(element)

    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output

assert subsets([9]) == [[], [9]]
assert sorted(subsets([9, 10])) == sorted([[], [9], [10], [9, 10]])
def max_sum_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for element in arr[1:]:
        current_sum = max(current_sum + element, element)

        max_sum = max(current_sum, max_sum)

    return max_sum


assert max_sum_subarray([1, 2, 3, -4, 6]) == 8
assert max_sum_subarray([1, 2, -5, -4, 1, 6]) == 7
assert max_sum_subarray([-12, 15, -13, 14, -1, 2, 1, -5, 4]) == 18
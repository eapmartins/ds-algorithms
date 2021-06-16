def add_one(arr):

    borrow = 1

    for i in range(len(arr), 0, -1):
        digit = borrow + arr[i - 1]

        borrow = digit//10

        if borrow == 0:
            arr[i -1] = digit
            break
        else:
            arr[i - 1] = digit % 10

    arr = [borrow] + arr
    pos = 0
    
    if arr[pos] == 0:
        pos += 1

    return arr[pos:]

assert add_one([1, 2, 3]) == [1, 2, 4]
assert add_one([1, 2, 9]) == [1, 3, 0]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]
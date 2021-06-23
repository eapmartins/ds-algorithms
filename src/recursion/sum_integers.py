def sum_integers(n):
    if n == 1:
        return 1

    return n + sum_integers(n - 1)

assert sum_integers(3) == 6
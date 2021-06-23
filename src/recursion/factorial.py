def factorial(n):
    """
    Calculate n!
    
    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """

    if n == 1 or n == 0:
        return 1

    return n * factorial(n - 1)

assert factorial(6) == 720
assert factorial(0) == 1
assert factorial(5) == 120
assert factorial(1) == 1
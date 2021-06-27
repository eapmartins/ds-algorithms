"""
param: n - number of steps in the staircase
Return number of possible ways in which you can climb the staircase
"""
def staircase(n):
    if n <= 0:
        return 1
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)

assert staircase(3) == 4
assert staircase(4) == 7
assert staircase(5) == 13
assert staircase(7) == 44
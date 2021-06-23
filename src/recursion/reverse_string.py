def reverse_string(input):

    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that is the reverse of input
    """

    if len(input) == 1:
        return input[0]

    return input[-1] + reverse_string(input[:-1])

assert reverse_string("abcde") == "edcba"
assert reverse_string("edson") == "nosde"
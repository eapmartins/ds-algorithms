from src.stack.stack import Stack

def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of breacket reversals needed
    """
    
    if len(input_string) % 2 != 0:
        return -1
    
    
    stack = Stack()
    open_bracket = 0
    close_bracket = 0

    for bracket in input_string:
        if bracket == '{':
            stack.push(bracket)
            open_bracket += 1
        elif bracket == '}' and stack.top() == '{':
            stack.pop()
            open_bracket -= 1
        elif bracket == '}' and stack.top() != '{':
            stack.push(bracket)
            close_bracket += 1
    
    return int(open_bracket / 2 + close_bracket / 2)


assert minimum_bracket_reversals("}{{}}{{{") == 2
assert minimum_bracket_reversals("{{{") == -1
assert minimum_bracket_reversals("{}{}") == 0
assert minimum_bracket_reversals("}}") == 1
assert minimum_bracket_reversals("}}}}") == 2
assert minimum_bracket_reversals("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}") == 13
assert minimum_bracket_reversals("}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}") == 1
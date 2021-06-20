from src.stack.stack import Stack

def equation_checker(equation):
    stack = Stack()

    for char in equation:
        if char == '(':
            stack.push(char)
        
        if char == ')' and stack.pop() == None:
            return False

    return stack.size() == 0
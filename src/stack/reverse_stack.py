from src.stack.stack import Stack

def reverse_stack(stack):
    new_stack = Stack()
    
    while not stack.is_empty():
        new_stack.push(stack.pop())

    return new_stack
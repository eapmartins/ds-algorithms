from src.stack.stack import Stack

def reverse_queue(queue):
    """
    Reverese the input queue

    Args:
       queue(queue),str2(string): Queue to be reversed
    Returns:
       queue: Reveresed queue
    """
    
    stack = Stack()

    while not queue.is_empty():
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())

    return queue
from src.base.node import Node

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.queue_size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.queue_size += 1
        
    def dequeue(self):
        
        if self.is_empty():
            return None

        head = self.head
        self.head = self.head.next        
        self.queue_size -= 1

        return head.value

    def peek(self):
        if self.is_empty():
            return None

        return self.head

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0
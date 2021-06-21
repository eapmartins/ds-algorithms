from src.base.node import Node

class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            return None

        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1

        return value

    def top(self):
        if self.head is None:
            return None

        return self.head.value
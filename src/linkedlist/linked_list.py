from base.node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        
        while node:
            out.append(node.value)
            node = node.next
        return out

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        aux = Node(value)
        aux.next = self.head
        self.head = aux

    def append(self, value):
        
        if self.head is None:
            self.head = Node(value)
            return
        
        aux = self.head
        while aux.next:
            aux = aux.next
        
        aux.next = Node(value)

    def search(self, value):
        
        if self.head is None:
            return None

        aux = self.head
        while aux:
            if aux.value == value:
                return aux
            aux = aux.next

    def remove(self, value):
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return

        aux =  self.head
        while aux.next:
            if aux.next.value == value:
                aux.next = aux.next.next
                return
            aux = aux.next

    def pop(self):
        if self.head is None:
            return None

        aux = self.head
        self.head = self.head.next

        return aux.value

    def insert(self, value, pos):

        if self.head is None:
            self.head = Node(value)
            return

        if pos == 0:
            self.prepend(value)
            return

        index = 0
        aux = self.head

        while aux.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = aux.next
                aux.next = new_node
                return
            index += 1
            aux = aux.next
        else:
            self.append(value)

    def size(self):
        size = 0
        aux = self.head
        while aux:
            size += 1
            aux = aux.next

        return size

    def reverse(self):
        if self.head is None:
            return None
        
        new_list = LinkedList()
        aux = self.head

        while aux:
            new_list.prepend(aux.value)
            aux = aux.next
        
        return new_list

    def iscircular(self):
        
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
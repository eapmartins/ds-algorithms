class Queue:

    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):

        if self.queue_size == len(self.arr):
            self._handle_full_capacity()

        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index += 1
        
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        
        dequeued = self.peek()

        if self.is_empty():
            self.front_index = -1
            self.next_index = 0
            return None
        
        for i in range(self.queue_size):
            self.arr[i] = self.arr[i + 1]
        
        self.next_index -= 1
        self.queue_size -= 1

        return dequeued

    def peek(self):
        if self.is_empty():
            return None

        return self.arr[self.front_index]

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def _handle_full_capacity(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(len(old_arr) * 2)]
        self.next_index = 0

        for i in range(len(old_arr)):
            self.arr[i] = old_arr[i]
            self.next_index += 1
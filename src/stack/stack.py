class Stack:

    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, value):

        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity.")
            self.handle_stack_capacity_full()

        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1

    def handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range(2 * len(old_arr))]

        for index, value in enumerate(old_arr):
            self.arr[index] = value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None

        self.next_index -= 1
        self.num_elements -= 1

        return self.arr[self.next_index]

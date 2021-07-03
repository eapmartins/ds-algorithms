class HuffmanNode:
    def __init__(self, value, weight):
        self.left = None
        self.right = None
        self.value = value
        self.weight = weight        
    
    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return str(self.value) + " " + str(self.weight)
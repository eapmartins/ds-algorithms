from src.trees.node import Node

class Tree(object):

    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root
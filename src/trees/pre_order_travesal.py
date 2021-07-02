from src.trees.tree import Tree
from src.trees.node import Node

def pre_order_travesal(tree):

    visit_order = list()
    root = tree.get_root()
    

    def traverse(root):
        
        if root:
            visit_order.append(root.get_value())
            traverse(root.get_left_child())
            traverse(root.get_right_child())

    traverse(root)
    
    return visit_order

tree = Tree('a')
root = tree.get_root()

b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

root.set_left_child(b)
root.set_right_child(e)

b_child = root.get_left_child()
b_child.set_left_child(c)
b_child.set_right_child(d)

e_child = root.get_right_child()
e_child.set_left_child(f)

f_child = e_child.get_left_child()

f_child.set_left_child(g)
f_child.set_right_child(h)

assert pre_order_travesal(tree) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
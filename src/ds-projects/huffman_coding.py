import sys
import heapq
from src.base.huffman_node import HuffmanNode

def create_nodes(data):
    frequencies = dict()
    nodes = list()
    
    for char in data:
        frequencies[char] = frequencies.get(char, 0) + 1

    for key in frequencies.keys():
        nodes.append(HuffmanNode(key, frequencies.get(key)))

    return nodes

def create_tree(nodes):
    heap = nodes
    heapq.heapify(nodes)
    
    while len(heap) != 1:
        internal = HuffmanNode(None, None)
        left = heapq.heappop(heap)
        internal.left  = left
        right = heapq.heappop(heap)
        internal.right  = right
        internal.weight = left.weight + right.weight
        heapq.heappush(heap, internal)
    
    return heap

def create_encoding_table(root):
    encoding_table = {}

    def get_code(node, current_code=""):
        
        if (node == None): 
            return
        
        if (node.left == None and node.right == None):
            encoding_table[node.value] = current_code

        get_code(node.left, current_code + "0")
        get_code(node.right, current_code + "1")

    get_code(root[0])

    return encoding_table

def huffman_encoding(data):
    nodes = create_nodes(data)
    tree = create_tree(nodes)
    encoding_table = create_encoding_table(tree)
    encoded_data = ""
    
    for item in data:
       encoded_data += encoding_table[item]
    
    return encoded_data, tree

def huffman_decoding(data, tree):

    decoded = ""
    root = tree[0]

    for bit in data:
        
        if bit == '0':
            root = root.left
        
        elif bit == '1':
            root = root.right
        
        if root.value:
            decoded += root.value
            root = tree[0]        

    return decoded
    
a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

assert encoded_data  == "1010101010101000100100111111111111111000000010101010101"

assert decoded_data == a_great_sentence
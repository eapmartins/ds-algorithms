from src.linkedlist.linked_list import LinkedList

"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped
"""
def swap_nodes(head, position_one, position_two):

    if position_one == position_two:
        return head
    
    left_node_position_one = None
    node_position_one = None

    left_node_position_two = None
    node_position_two = None

    current_index = 0
    current_node = head 
    new_head = None

    while current_node:

        if current_index == position_one:
            node_position_one = current_node
        
        elif current_index == position_two:
            node_position_two = current_node
            break

        if node_position_one is None:
            left_node_position_one = current_node
        
        left_node_position_two = current_node
        
        current_node = current_node.next         
        current_index += 1
        
    
    left_node_position_two.next = node_position_one
    temp = node_position_one.next
    node_position_one.next = node_position_two.next
    node_position_two.next = temp
    
    # if the node at first index is head of the original linked list
    if left_node_position_one is None:
        new_head = node_position_two
    else:
        left_node_position_one.next = node_position_two
        new_head = head
    
    return new_head


linkedlist = LinkedList()
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)

result = swap_nodes(linkedlist.head, 1, 2)

while result:
    print(result.value)
    result = result.next
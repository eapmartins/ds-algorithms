from src.linkedlist.linked_list import LinkedList

def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    
    if i == 0:
        return None

    if j == 0:
        return head

    if head is None or j < 0 or i < 0:
        return head

    current = head
    previous = None

    while current:
        
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next

        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node

        previous.next = current
    
    return head
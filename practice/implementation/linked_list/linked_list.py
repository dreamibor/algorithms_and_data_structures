"""
Define linked list node and helper functions.
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val}"
    
    def __lt__(self, other):
        # Used for min heap.
        return self.val < other.val

def traverse(head: ListNode) -> str:
    """ Traverse linked list from head node.
    """
    current = head
    result = []
    while current:
        result.append(f"{current.val}")
        current = current.next
    result.append("None")
    return " -> ".join(result)

def create_linked_list(input_list: list) -> ListNode:
    """ Create linked list from a list.
    """
    if not input_list:
        raise ValueError("Empty input list!")

    dummy = ListNode(0)
    current = dummy

    for elemment in input_list:
        current.next = ListNode(elemment)
        current = current.next
    
    return dummy.next

if __name__=="__main__":
    head = create_linked_list([1, 2, 3])
    print(traverse(head))
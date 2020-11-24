"""
Linked List - Reorder List (medium)

Description:
Given a singly linked list L: L0 → L1 → … → Ln-1 → Ln,
reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

Note:
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Input: 1->2->3->4
Output: 1->4->2->3

LeetCode link: https://leetcode-cn.com/problems/reorder-list/
"""
from linked_list import ListNode, create_linked_list, traverse


def reorder_list_array(head: ListNode) -> ListNode:
    """ Using Array to Access Index.
    Linked list doesn't support using index to randomly access elements.
    We can use an array (linear list) to store the linked list and then 
    rebuild the linked list using index.

    Time Complexity - O(N) - N is the number of elements of the list.
    Space Complexity - O(N) - For the linear list. 
    """
    if not head: return head

    store_list = []
    current = head

    while current:
        store_list.append(current)
        current = current.next

    i, j = 0, len(store_list) - 1

    while i < j:
        store_list[i].next = store_list[j]
        
        i += 1

        if i == j: break

        store_list[j].next = store_list[i]

        j -= 1
    
    store_list[i].next = None

    return head

def reorder_list(head: ListNode) -> ListNode:
    """ Find Middle Node + Reverse List + Merge List
    The target linked list is a result of merging the left part and the 
    reversed right part. So we can fulfill this task in three steps:
    1. Find the middle node of the linked list.
    2. Reverse the right half of the original linked list.
    3. Merge the left half and reversed right half.

    Time Complexity - O(N) - N is the number of nodes.
    Space Complexity - O(1) - For constant number of pointers.
    """
    def find_middle(head: ListNode) -> ListNode:
        """ Find middle using fast and slow pointers. """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(head: ListNode) -> ListNode:
        """ Reverse with iteration. """
        prev, current = None, head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    
    def merge(l1: ListNode, l2: ListNode) -> ListNode:
        """ Merge two lists one element by one. """
        while l1 and l2:
            l1_temp = l1.next
            l2_temp = l2.next

            l1.next = l2
            l1 = l1_temp

            l2.next = l1
            l2 = l2_temp
    
    mid = find_middle(head)

    # Break down two lists to l1 and l2
    l1 = head
    l2 = mid.next
    mid.next = None
    # Reverse l2
    l2 = reverse(l2)
    # Merge l1 and l2 one by one.
    merge(l1, l2)      

    return head

if __name__ == "__main__":
    head = create_linked_list([1,2,3,4,5])
    result = reorder_list_array(head)
    print(traverse(result))

    head = create_linked_list([1,2,3,4,5])
    result = reorder_list(head)
    print(traverse(result))

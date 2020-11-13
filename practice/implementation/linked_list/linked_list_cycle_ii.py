"""
Linked List - Linked List Cycle II (easy)

Given the head of a singly linked list that contains a cycle, write a function 
to find the starting node of the cycle, if there is no cycle return None.

Example:
Input: head = [3,2,0,-4], pos = 1 (cycle postion)
Output: Return the node at index 1.
Explanation: There is a cycle in the linked list, linking from the last node 
to the second node (with index 1).

LeetCode link: https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""
from linked_list import ListNode


def start_of_cycle(head: ListNode) -> ListNode:
    """ Fast and Slow Pointers
    We first us fast and slow pointers to find the meeting 
    point of fast and slow point.

    Assume from head to cycle entrance is a, when slow has 
    entered the cycle, it walked b to meeting point and c 
    is the remaining length of the cycle. 

    Fast has walked in the cycle for n times to meet slow, 
    so the total distance fast has travelled is 
    a + n(b+c) + b = a + (n+1)b + nc
    The slow pointer has travelled a + b, as we've known, 
    the fast travels two times faster than slow, so
    a + (n+1)b +nc = 2(a+b) => a = c + (n-1)(b+c)

    Time Complexity - O(N) - N is the total number of elements in the LinkedList.
    Space Complexity - O(1) - For three pointers.
    """
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            pointer1 = fast
            pointer2 = head

            while pointer1 != pointer2:
                pointer1 = pointer1.next
                pointer2 = pointer2.next
            
            return pointer2

    return None

def start_of_cycle_hash_table(head: ListNode) -> ListNode:
    """ Hash Table
    We record every node we've seen, if we have met a node 
    that has shown before (the first repeat node), then is 
    must be the entrance of the cycle.

    Time Complexity - O(N) - iterate through the list.
    Space Complexity - O(N) - for hash set.
    """
    seen = set()

    while head:
        if head in seen:
            return head
        
        seen.add(head)
        head = head.next
    
    return None


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    print(start_of_cycle(head))
    print(start_of_cycle_hash_table(head))

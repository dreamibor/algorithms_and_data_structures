"""
Linked List - Sort List (medium)

Description:
Given the head of a linked list, return the list after sorting it in ascending order.

Example:
Input : [4,2,1,3]
Output: [1,2,3,4]

Notes:
1. Can you sort the linked list in O(n*logn) time and O(1) memory (i.e. constant space)?

LeetCode link: https://leetcode-cn.com/problems/sort-list/
"""
from linked_list import ListNode, create_linked_list, traverse


def sort_list_top_down(head: ListNode) -> ListNode:
    """ Merge Sort - Top-down Recursion
    The process of top-down merge sort on linked lists is:
    1. Find the middle of the linked list, break down the list into two sub-lists.
    2. Sort the two sub-lists.
    3. Merge the two sorted sub-lists, and return the full sorted list (merge two sorted list).

    Since we are using recursion to implement merge sort, we need to define the stop condition.
    Here it's when the number of nodes in a list is less than or equal to 1 (when the list is 
    empty or only contains one node).

    Time Complexity - O(N*logN)
    Space Complexity - O(logN) - For recursion stack.
    """
    # Termination condition.
    if not head or not head.next: return head

    # Find the middle of the linked list.
    slow, fast = head, head.next

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    # Cut the list at the mid index.
    mid, slow.next = slow.next, None

    # Recursion for left and right part.
    left, right = sort_list_top_down(head), sort_list_top_down(mid)

    # Merge two sorted list.
    dummy = ListNode(0)
    current = dummy

    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
    
    current.next = left if left else right

    return dummy.next

def sort_list_bottom_up(head: ListNode) -> ListNode:
    """ Merge Sort - Bottom-up
    To meet the requirement using O(1) space complexity, we need to implement 
    merge sort using bottom-up method.

    1. Find the length of the linked list, interval < length.
    2. Interval starting from 1, representing the sub-list length to be sorted.
    3. Break the list into several sub-lists, and merge those sub-lists in pairs.
    4. Double the value of interval, repeat step 3 until the sub-list length is 
    larger than or equal to length.

    Time Complexity - O(N*logN)
    Space Complexity - O(logN) - For recursion stack.
    """
    # Get the length of the linked list.
    current = head
    length = 0
    while current:
        current = current.next
        length += 1
    
    # Initial interval length: 1, 2, 4, ...
    interval = 1

    # Dummy node to locate head
    dummy = ListNode(0)
    dummy.next = head

    while interval < length:
        prev, cur = dummy, dummy.next

        while cur:
            # For each interval round, find merge unit 1 and 2, called h1 and h2.
            h1, i = cur, interval
            while i and cur:
                cur = cur.next
                i -= 1
            
            # No need to merge since we've reached the end (h2 is None).
            if i: break

            h2, i = cur, interval

            # Calculate the length of h1 and h2.
            # The length of h2 could be smaller than interval.
            # The length of h2 is c2 = interval - i.
            while i and cur:
                cur = cur.next
                i -= 1

            c1, c2 = interval, interval - i

            # Merge h1 and h2
            while c1 and c2:
                if h1.val < h2.val:
                    prev.next = h1
                    h1 = h1.next
                    c1 = c1 - 1
                else:
                    prev.next = h2
                    h2 = h2.next
                    c2 = c2 - 1
                
                prev = prev.next

            prev.next = h1 or h2

            # Move prev to the node before cur.
            while c1 > 0 or c2 > 0:
                prev = prev.next
                c1 -= 1
                c2 -= 1
            
            prev.next = cur

        interval *= 2
    
    return dummy.next


if __name__ == "__main__":
    head = create_linked_list([4,2,1,3])
    result = sort_list_top_down(head)
    print(traverse(result))

    head = create_linked_list([4,2,1,3])
    result = sort_list_bottom_up(head)
    print(traverse(result))






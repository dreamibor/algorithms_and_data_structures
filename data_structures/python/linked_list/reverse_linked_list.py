"""
Linked List - Reverse LinkedList Cycle (easy)

Description:
Reverse a singly linked list (in-place).

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

LeetCode link: https://leetcode-cn.com/problems/reverse-linked-list/
"""

from singly_linked_list import Node, LinkedList


def reverse_linked_list(head: Node) -> Node:
    """ Solution - Iteration
    Time Complexity - O(N) - iterate through the linked list.
    Space Complexity - O(1) - for temporary pointers.
    """
    prev = None
    current = head

    while current:
        temp = current.next # Temporarily store the next node of current.
        current.next = prev # Reverse the current node, change it's next to prev.
        prev = current # Assign the current node to prev
        current = temp # current becomes the current.next node.
    
    return prev


def reverse_linked_list_recursion(head: Node) -> Node:
    """ Solution - Recursion
    Time Complexity - O(N) - iterate through the linked list.
    Space Complexity - O(N) - since we are using recursion, so it will 
    call recursion stack.

    For better understanding with slides:
    https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
    """

    # Recursion stop condition, the current node is None or
    # the next node is None. For example, for linked list 
    # 1 -> 2 -> 3 -> None, it will stop at node 3 and return it.
    if head == None or head.next == None:
        return head
    
    # Temp will be the last node, in this case, 3.
    temp = reverse_linked_list_recursion(head.next)
    # Assume all nodes after the current node's next node are all 
    # reversed, now we need to reverse the next node and the 
    # current node.For example, when 3 is returned, temp will be 3, 
    # while head will be 2, and 2.next.next is now assigned to 2 
    # which means 3.next = 2, so the node is reversed.
    head.next.next = head
    # To avoid a list loop, we need to set head.next to None, in 
    # this case, 2.next is set to None for now.
    head.next = None

    # Return the last node or the first node in the reversed list.
    # Here it's 3.
    return temp


if __name__ == "__main__":
    new_list = LinkedList([1,2,3,4,5,6])
    print(f"Linked List: {new_list}")

    new_head = reverse_linked_list(new_list.head)
    reversed_list = LinkedList()
    reversed_list.head = new_head
    print(f"Linked List: {reversed_list}")

    new_list = LinkedList([1,2,3,4,5,6])
    print(f"Linked List: {new_list}")
    reversed_head = reverse_linked_list_recursion(new_list.head)
    new_reversed_list = LinkedList()
    new_reversed_list.head = reversed_head
    print(f"Linked List: {new_reversed_list}")
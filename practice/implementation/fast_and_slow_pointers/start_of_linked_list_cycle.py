"""
Fast and slow pointers - Start of LinkedList Cycle (medium)

Description:
Given the head of a Singly LinkedList that contains a cycle, write a function 
to find the starting node of the cycle.

Example:
Input: head = [3,2,0,-4], pos = 1 (cycle postion)
Output: Return the node at index 1.
Explanation: There is a cycle in the linked list, linking from the last node 
to the second node (with index 1).

Time Complexity - O(N) - N is the total number of elements in the LinkedList.
Space Complexity - O(1) - For two pointers.

LeetCode link: https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""


class ListNode:
    # Define singly linked list.
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

"""
Solution 1 - Moving a pointer K (the length of cycle) ahead.
We can take two pointers, pointer1 and pointer2. Initialise both pointers at the 
start of the linked list. We can then find the length of the cycle K first. Then 
we can move pointer2 ahead by K nodes, then we keep incrementing pointer1 and 
pointer2 until they both meet. 
As pointer 2 is K nodes ahead of pointer1, which means pointer2 must have completed 
one loop in the cycle when both pointers meet. Their meeting point will be the start 
of the cycle.
"""

def calculate_cycle_length(slow: ListNode) -> int:
    current = slow
    cycle_length = 0

    while True:
        current = current.next
        cycle_length += 1

        if  current == slow:
            break
    
    return cycle_length

def find_start(head: ListNode, cycle_length:int) -> ListNode:
    pointer1 = head
    pointer2 = head

    # Move pointer2 ahead by K (cycle_length) nodes.
    while cycle_length:
        pointer2 = pointer2.next
        cycle_length -= 1
    
    # Increment both pointers until they meet at the start of the cycle.
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    return pointer1


def find_cycle_start(head: ListNode) -> ListNode:
    cycle_length = 0

    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            cycle_length = calculate_cycle_length(slow)
            break
    
    return find_start(head, cycle_length)


"""
Solution 2 - Find the meeting point and then move

Similar to the above solution, move pointer1 to the meeting pointer first, and 
then increment both pointer1 and pointer2, until they meet.

Time Complexity - O(N) - N is the total number of elements in the LinkedList.
Space Complexity - O(1) - For two pointers.

Mathematical prove: https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/142-huan-xing-lian-biao-ii-jian-hua-gong-shi-jia-2/
"""

def detect_cycle_start(head: ListNode):
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        # Meeting point
        if fast == slow:
            # Pointer1 at meeting point while pointer2 at the head.
            pointer1 = fast
            pointer2 = head

            while pointer1 != pointer2:
                pointer1 = pointer1.next
                pointer2 = pointer2.next
            
            return pointer2
    
    return None


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))
    print("LinkedList cycle start: " + str(detect_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))
    print("LinkedList cycle start: " + str(detect_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))
    print("LinkedList cycle start: " + str(detect_cycle_start(head).value))


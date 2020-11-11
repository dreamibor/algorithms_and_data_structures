"""
Fast and slow pointers - LinkedList Cycle (easy)

Description:
Given the head of a Singly LinkedList, write a function to determine if the 
LinkedList has a cycle in it or not.

Example:
Input: head = [3,2,0,-4], pos = 1 (cycle postion)
Output: True
Explanation: There is a cycle in the linked list, linking from the last node 
to the second node.

Notes:
1. We can use hash table to record the nodes we've seen, and check whether a 
node is already in the hash table. This will take O(N) for space complexity, 
so try with constant space complexity solution.

Time Complexity - O(N) - N is the total number of elements in the LinkedList.
Space Complexity - O(1) - For two pointers.

LeetCode link: https://leetcode-cn.com/problems/linked-list-cycle/
"""


class ListNode:
    # Define singly linked list.
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        # Fast moves two steps while slow moves one step.
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            # Found the cycle if fast catched up slow.
            return True
    
    return False


"""
Similar Problem - LinkedList Cycle Length (easy)

Description:
Given the head of a LinkedList with a cycle, find the length of the cycle.

Time Complexity - O(N) - N is the total number of elements in the LinkedList.
Space Complexity - O(1) - For two pointers.

LeetCode link: 
"""


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0

    # Iterate and count the nodes cycle.
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    
    return cycle_length


def find_cycle_length(head: ListNode) -> int:
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            # Found the cycle and then calculate the cycle length.
            return calculate_cycle_length(slow)

    return 0


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("LinkedList cycle length: " + str(find_cycle_length(head)))
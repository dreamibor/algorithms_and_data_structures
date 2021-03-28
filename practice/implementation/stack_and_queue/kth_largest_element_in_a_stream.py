"""
Priority Queue (Heap Queue) - Kth Largest Element in a Stream (easy)

Description:
Design a class to find the kth largest element in a stream. Note that it is the kth largest 
element in the sorted order, not the kth distinct element.

Implement KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of 
integers `nums`.
- int add(int val) Returns the element representing the kth largest element in the stream.

Example:
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output:
[null, 4, 5, 5, 8, 8]
Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

LeetCode Link: https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/
"""
import heapq

class KthLargest:
    """ Using Python built-in heapq (Min heap, the smallest element is always the root heap[0]). 
    Heapq docs:
    - heapq.heappush(heap, item)
        Push the value item onto the heap, maintaining the heap invariant (unchanged).
    - heapq.heappop(heap)
        Pop and return the smallest item from the heap, maintaining the heap invariant. 
        If the heap is empty, IndexError is raised.
    - heapq.heappushpop(heap, item)
        Push item on the heap, then pop and return the smallest item from the heap. The combined 
        action runs more efficiently than heappush() followed by a separate call to heappop().
    - heapq.heapify(x)
        Transform list x into a heap, in-place, in linear time.
    """
    def __init__(self, k: int, nums: list):
        self.k = k
        self.heap = nums

        # Heapify the array to a min-heap.
        heapq.heapify(self.heap)

        # While there are more than k elements in the heap,
        # pop the smallest element out until we have k elements.
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        # Push the new element into heap.
        heapq.heappush(self.heap, val)
        # Pop elements out to keep k elements in the heap.
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # Return the root.
        return self.heap[0]


# TODO: Implement min-heap by myself.
  

if __name__ == "__main__":
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    kth_largest = kthLargest.add(3);   # return 4
    print(kth_largest)
    kth_largest = kthLargest.add(5);   # return 5
    print(kth_largest)
    kth_largest = kthLargest.add(10);  # return 5
    print(kth_largest)
    kth_largest = kthLargest.add(9);   # return 8
    print(kth_largest)
    kth_largest = kthLargest.add(4);   # return 8
    print(kth_largest)
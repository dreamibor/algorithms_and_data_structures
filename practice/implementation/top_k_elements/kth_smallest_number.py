"""
Heap - Kth Smallest Number (easy)

Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, 
not the Kth distinct element.

Example:
Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller 
numbers are [1, 2].

Educative: https://www.educative.io/courses/grokking-the-coding-interview/gxxPGn8vE8G 
"""
import heapq


def kth_largest_heap(nums: list, k: int) -> int:
    """ Max Heap

    Max heap - using negative values with min heap.

    We can have a heap of size k whose heap top will be the kth smallest (or 
    the minimum in the heap), after iterating through the array, we can just 
    return the heap top as the result.

    Time Complexity - O(NlogK) - N for iterating through the array, logk for 
    readjusting the heap sorted.
    Space Complexity - O(K) - For the heap.
    """
    heap = []

    for num in nums:
        # Push the new element into the heap.
        heapq.heappush(heap, -num)

        # Pop the heap top if there are more than K elements.
        if len(heap) > k:
            heapq.heappop(heap)

    return -heap[0]


def kth_largest_min_heap(nums: list, k: int) -> int:
    """ Min Heap

    We can also use min heap, push all elements into the min heap and then 
    pop out top k elements from the heap, and the kth element will be the 
    answer. 

    Time Complexity - O(N+KlogN) - Initializing the min-heap with all numbers 
    will take O(N) and extracting K numbers will take O(KlogN).
    Space Complexity - O(N) - For the heap.
    """
    heap = []

    for num in nums:
        # Push all the elements into the heap.
        heapq.heappush(heap, num)
    
    # Get the kth smallest element.
    res = 0
    while k:
        res = heapq.heappop(heap)
        k -= 1

    return res

if __name__ == "__main__":
    nums, k = [1, 5, 12, 2, 11, 5], 3
    print(kth_largest_heap(nums, k))
    print(kth_largest_min_heap(nums, k))

    nums, k = [5, 12, 11, -1, 12], 3
    print(kth_largest_heap(nums, k))
    print(kth_largest_min_heap(nums, k))
"""
Queue - Sliding Window Maximum (hard)

Description:
You are given an array of integers `nums`, there is a sliding window of size `k` which is 
moving from the very left of the array to the very right. You can only see the `k` numbers 
in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Follow up: could you solve the problem with linear time complexity O(N)?

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
--------------------------    -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

LeetCode Link: https://leetcode-cn.com/problems/sliding-window-maximum/
"""


def max_sliding_window_brute_force(nums: list, k: int) -> list:
    """ Brute Force
    Sliding the size k window through the array and append all the 
    maximum into a result array.

    Time Complexity - O(N*k) - There are N - k + 1 sliding windows in 
    total, and each window has a size of k, to find the maximum, we need 
    O(k) for each window, so in total O(N*k).
    Space Complexity - O(N-k+1) - For the output array.

    The program will usually run out of time on Online Judge platforms.
    """
    # Edge cases
    if not nums: return []

    result = []

    for index in range(len(nums) - k + 1):
        result.append(max(nums[index: index+k]))

    return result

def max_sliding_window_heapq(nums: list, k: int) -> list:
    """ Priority Queue (Max Heap, using negative values in Min Heap)

    1. Adjust heap - O(logk)
    2. Extract max from the top - O(1)

    Time Complexity - O(N*logK) - size N for 
    Space Complexity - O(N-k+1) - For the output array.
    """
    # Edge cases
    if not nums: return []

    import heapq

    # Max heap - using negative values in min heap.
    max_heap = [(-nums[i], i) for i in range(k)]
    heapq.heapify(max_heap)

    # Initialize the first maximum value.
    result = [-max_heap[0][0]]

    for i in range(k, len(nums)):
        # Push one new element into the heap.
        heapq.heappush(max_heap, (-nums[i], i))

        # If the maximum is out of the window,
        # remove it from the heap.
        while max_heap[0][1] <= i - k:
            heapq.heappop(max_heap)
        
        # Append the maximum into the result array.
        result.append(-max_heap[0][0])
    
    return result


def max_sliding_window_deque(nums: list, k: int) -> list:
    """ Double-ended Queue (monotonic decreasing deque)

    Assuing index i and j, and i is on the left on j (i < j), also the corresponding 
    num of i is smaller than j (nums[i] <= nunms[j]), then as long as i is still in 
    the window, then i could be the maximum as j is the maximum, so we can remove 
    nums[i] from the queue. 

    When we are sliding the window and adding a new element, to keep the deque is 
    monotonic decreasing, we can compare the new element with the last element in the 
    deque, and remove the last element if it's smaller than the new element. Keep 
    removing until the window/deque is empty or the last element in the deque is larger 
    than the new element. 

    Time Complexity - O(N) - Every element's index is only put into/pop out of 
    the deque once.
    Space Complexity - O(N-k+1) - For the output array.
    """
    # For edge cases.
    if not nums: return []

    window, result = [], []

    for i, x in enumerate(nums):
        # Remove the left most element since it's out of the window.
        if i >= k and i - k >= window[0]:
            window.pop(0)
        # If x is larger than the maximum of the original max, then remove all 
        # elements before the original maximunm.
        while window and x >= nums[window[-1]]:
            window.pop()
        # Append the index of the new element into the window.
        window.append(i)
        # print("window: {}".format([nums[i] for i in window]))
        
        # Append maximum into the result array (it will be left most element in 
        # the deque since it's monotonic decreasing).
        if i >= k - 1:
            result.append(nums[window[0]])

    return result


if __name__ == "__main__":
    # Brute force
    print("Brute force: ")
    print(max_sliding_window_brute_force(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(max_sliding_window_brute_force(nums = [1], k = 1))
    print(max_sliding_window_brute_force(nums = [1, -1], k = 1))
    print(max_sliding_window_brute_force(nums = [4, -2], k = 2))
    # Max Heap
    print("Max Heap: ")
    print(max_sliding_window_heapq(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(max_sliding_window_heapq(nums = [1], k = 1))
    print(max_sliding_window_heapq(nums = [1, -1], k = 1))
    print(max_sliding_window_heapq(nums = [4, -2], k = 2))
    # Queue
    print("Queue: ")
    print(max_sliding_window_deque(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(max_sliding_window_deque(nums = [1], k = 1))
    print(max_sliding_window_deque(nums = [1, -1], k = 1))
    print(max_sliding_window_deque(nums = [4, -2], k = 2))
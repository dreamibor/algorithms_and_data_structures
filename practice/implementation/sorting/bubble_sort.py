"""
Sorting - Bubble Sort

Compare two adjacent elements, if left is larger than right, then swap them. 
For each bubble loop, there will be a largest number moved to right.
Run the bubble loop for N times to get the sorted array.

Time Complexity - O(N^2) - N is the number of elements in the array.
Space Complexity - O(1) - The variable for swapping elements.
"""


def bubble_sort_forward(nums: list) -> list:
    """ Forward

    Each time, we move the largest value to right. The current largest value 
    will be moved to position n - i - 1. For example, i = 0, the position is 
    n - 1, which will store the largest element in the array.
    """
    n = len(nums)

    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums

def bubble_sort_forward_early_stop(nums: list) -> list:
    """ Forward with Early Stopping
    If the array is already sorted (meaing there is no swapping operation 
    during the bubble loop), then we can stop the outer for loop.
    """
    n = len(nums)

    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap = True
        
        # Early stop as there are no elements to swap.
        if not swap:
            break
        
    return nums

def bubble_sort_backward(nums: list) -> list:
    """ Backward

    The same logic as forward, but using the value of outer loop to control 
    the range of inner loop directly. The outer loop is used to control the 
    inner loop to run N times, so we can start from N to 0.
    """
    n = len(nums)
    
    # Equivalent to
    # for i in range(len(array) - 1, 0, -1):
    for i in reversed(range(n)):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums


if __name__ == "__main__":
    nums = [1,6,5,4,3,2,1]
    print(bubble_sort_forward(nums))
    print(bubble_sort_forward_early_stop(nums))
    print(bubble_sort_backward(nums))
    
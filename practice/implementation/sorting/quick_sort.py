"""
Sorting - Quick Sort

Each time, we choose a pivot, and split the array into two parts, elements on 
the left are smaller than pivot, and elements on the right are larger than 
pivot. We then process the two parts recursively until there is only one 
element remaining.

Quick is an in-place sorting algorithm while merge sort is not in-place.

Time Complexity - O(N*logN) - If we can split the two parts evenly each time, 
then the recursion tree is balanced, so the depth of the recursion tree is 
O(logN), and for each partition, we need to scan the array once, so in the 
best case, the time complexity will be O(N*logN). 

However, for most of the cases, we can't divide the array evenly, especially 
when the array is in the reversed order. So for the worst case, the time 
complexity will be O(N^2).

Space Complexity - O(1) - In-place sorting.

LeetCode: https://leetcode-cn.com/problems/sort-an-array/
"""
import random


def quick_sort_partition_rand(nums, l, r):
    """ Recursive partition function.

    quick_sort_partition(l, r) = 
    quick_sort_partition(l, i - 1) + i + quick_sort_partition(i + 1, r)

    i is the position of pivot.
    """
    # Recursion termination - there is only one element in the partition.
    if l >= r: return None

    # Randomly choose pivot here and exchange it with nums[r].
    # Split the array into two parts, smaller and larget than the pivot.
    # nums[l:i] is smaller than the pivot while nums[i:r] is large than the 
    # pivot.
    pivot_index = random.randint(l, r)
    nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
    pivot = nums[r]

    # i is to track the first index of right side (larger than the pivot).
    i = l
    for j in range(l, r):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    
    # Swap pivot and the first element of the right part.  
    nums[r], nums[i] = nums[i], nums[r]
    
    # Recursively process the left and right part, ignore pivot.
    quick_sort_partition_rand(nums, l, i - 1)
    quick_sort_partition_rand(nums, i + 1, r)

def quick_sort_partition(nums, l, r):
    """ Recursive partition function.

    quick_sort_partition(l, r) = 
    quick_sort_partition(l, i - 1) + i + quick_sort_partition(i + 1, r)

    i is the position of pivot.
    """
    # Recursion termination - there is only one element in the partition.
    if l >= r: return None

    # Split the array into two parts, smaller and larget than the pivot.
    # nums[l:i] is smaller than the pivot while nums[i:r] is large than the 
    # pivot.
    pivot = nums[r]

    # i is to track the first index of right side (larger than the pivot).
    i = l
    for j in range(l, r):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    
    # Swap pivot and the first element of the right part.  
    nums[r], nums[i] = nums[i], nums[r]
    
    # Recursively process the left and right part, ignore pivot.
    quick_sort_partition(nums, l, i - 1)
    quick_sort_partition(nums, i + 1, r)

def quick_sort(nums: list) -> list:
    # Edge cases
    if len(nums) <= 1: return nums

    # quick_sort_partition(nums, 0, len(nums) - 1)
    quick_sort_partition_rand(nums, 0, len(nums) - 1)

    return nums

if __name__ == "__main__":
    nums = [1,6,5,4,3,2,1]
    print(quick_sort(nums))

    nums = [5,1,1,2,0,0]
    print(quick_sort(nums))
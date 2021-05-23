"""
Sorting - Merge Sort

Merge Sort is based on divide and conquer. For a given array with length n, 
each time, we split it into two sub-arrays with length of n/2. We then 
recursively partition the arrays until there is only one element. Then we 
begin to merge the arrays.

Time Complexity - O(N*logN) - Each time we split the array recursively into 
two parts, so there are O(logN) partitions, and we need to merge two 
partitions with O(N), so in total O(N*logN).
Another explanation, the time complexity in the recursion form:
T(n)=2T(n / 2​) + O(n)
According to the master theorem, the ime complexity is O(N*logN).

Space Complexity - O(N) - We need O(N) extra space for the temp array. The 
recursion stack may at most take O(logN), so in total O(N+logN) = O(N). 

LeetCode: https://leetcode-cn.com/problems/sort-an-array/
"""


def merge(nums, l, mid, r):
    """ Linearly merge two sorted arrays into one. """
    temp = []
    # Starting position for two sorted arrays.
    i, j = l, mid + 1

    # Compare the elements in the two sorted array, and merge the 
    # smaller one into the temp array.
    while i <= mid and j <= r:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    # Add the remaining elements into temp array.
    temp += nums[i:mid+1] + nums[j:r+1]
    # Update the original array with temp array.
    nums[l: r+1] = temp


def merge_sort_partition(nums, l, r):
    """ Merge sort recursion function to sort [l,r].
    1. Calculate mid with l and r, mid = (l + r) // 2.
    2. Recursively sort [l, mid] with merge_sort_partition(nums, l, mid).
    3. Recursively sort [mid+1, r] with merge_sort_partition(nums, mid+1, r).
    4. Merge the two sorted arrays [l, mid] and [mid+1, r].
    """
    # Recursion termination
    if l >= r: return None

    # Partition
    mid = (l + r) // 2
    merge_sort_partition(nums, l, mid)
    merge_sort_partition(nums, mid + 1, r)

    # Merge the two sorted parts.
    merge(nums, l, mid, r)


def merge_sort(nums: list) -> list:
    # Edge cases
    if len(nums) <= 1: return nums

    merge_sort_partition(nums, 0, len(nums) - 1)

    return nums


if __name__ == "__main__":
    nums = [1,6,5,4,3,2,1]
    print(merge_sort(nums))

    nums = [5,1,1,2,0,0]
    print(merge_sort(nums))
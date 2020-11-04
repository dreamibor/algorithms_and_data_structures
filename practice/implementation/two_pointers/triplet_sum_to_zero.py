"""
Two pointers - Triplet Sum to Zero (medium)

Description:
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Notes:
1. The array is not sorted.
2. There are negative numbers in the array.
3. We need to find all unique triplets, so we have to skip any duplicate numbers.

Time Complexity - O(N^2) - N is the total number of elements in the given array.
Sorting the array will take O(N*logN). search_pair() function is taking O(N), and 
we are calling search_pair() for each number in the input array, so in total it 
will be O(N*logN + N^2), it's asymptotically equivalent to O(N^2).
Space Complexity - O(N) - space required for sorting, ignore the space needed for 
saving result.

LeetCode link: https://leetcode-cn.com/problems/3sum/
"""


def search_pair(arr, target, left, triplets):
    """ The function to search for a pair whose sum will be the given target.
    """
    right = len(arr) - 1

    # Loop while left is smaller than right.
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            triplets.append([-target, arr[left], arr[right]])

            # Move left and right one step further.
            left += 1
            right -= 1

            # Whether left is the same as the previous one.
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            
            # Whether right is the same as the previous one (on the right).
            while left < right and arr[right] == arr[right + 1]:
                right += 1


        elif target > current_sum:
            # The current sum is smaller, so need to increase the number by shift left.
            left += 1
        else:
            # The current sum is larger, so need to decrease the number by shift right.
            right -= 1


def search_triplets(arr: list) -> list:
    """ Approach: Sort and Find (with two pointers).
    We first sort the array, and then iterate through it taking one number
    at a time. When we are at number X, the target is to find a pair of whose sum is -X
    as X + Y + Z == 0.
    To find all the unique triplets, we've to skip any duplicate numbers. Since we will 
    sort the array, so all the duplicate numbers will be next to each other and are 
    easier to skip.
    """
    # Edge cases, array length smaller than 3.
    if len(arr) < 3:
        return []
    
    # Array to save results.
    triplets = []

    # Sort the array first - O(N*logN).
    arr.sort()

    # Iterate through the sorted array
    for i in range(len(arr)):
        # Since the array is sorted, if a is bigger than 0, then there is no chance that 
        # the sum of those following positive numbers can be zero, so return the result.
        if arr[i] > 0:
            return triplets
        # Skip when the current number if it's the same as previous one.
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        # Calling search pair (two sum) function.
        search_pair(arr, -arr[i], i+1, triplets)

    return triplets


def search_triplets_with_set(arr: list) -> list:
    """ Approach: U sing set
    Since a+b+c = 0, so c = -(a+b), with two embedded for loops and then using
    set to check whether c is in the array.

    Time Complexity - O(N^2) - two loops, searching set will be O(1).
    Space Complexity - O(N) - space required for set.

    Advantage: 
    1. Doesn't require to change the input array (no need to sort).
    2. Easier to understand.
    """
    if len(arr) < 3: return []

    arr.sort()

    res = set()

    for i, v in enumerate(arr[:-2]):
        if i > 0 and v == arr[i - 1]:
            continue
            
        d = {}

        for x in arr[i+1:]:
            if x not in d:
                d[-v-x] = 1
            else:
                res.add((v, -v-x, x))

    return [list(r) for r in res]


if __name__ == "__main__":
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))
    print(search_triplets([-1,0,1,2,-1,-4]))
    # All zeros
    print(search_triplets([0, 0, 0, 0]))
    # Test edge cases
    print(search_triplets([0]))
    print(search_triplets([]))
    # For testing the method using set.
    print(search_triplets_with_set([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets_with_set([-5, 2, -1, -2, 3]))
    print(search_triplets_with_set([-1,0,1,2,-1,-4]))
    print(search_triplets([0, 0, 0, 0]))
    print(search_triplets([0]))
    print(search_triplets([]))
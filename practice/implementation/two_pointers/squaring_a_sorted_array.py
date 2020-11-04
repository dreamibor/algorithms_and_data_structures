"""
Two pointers - Squaring a Sorted Array (easy)

Description:
Given a sorted array, create a new array containing squares of all the number 
of the input array in the sorted order.

Example:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Notes:
1. There are negative numbers in the array.
2. The output array shall be sorted.

Time Complexity - O(N) - N is the total number of elements in the given array.
Space Complexity - O(N) - the output array.

LeetCode link: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
"""


def make_squares(arr):
    """
    Numbers at both the ends can give us the largest square. Use two pointers starting
    at both ends, compare the square value at each step, move the bigger one into the 
    beginning of the new array using array.insert(0, value).
    """
    squares = [] # C-alike array initialisation: squares = [0 for x in range(n)]

    left = 0
    right = len(arr) - 1

    while left <= right:
        left_square = arr[left] ** 2
        right_square = arr[right] ** 2
        if left_square >= right_square:
            squares.insert(0, left_square)
            left += 1
        else:
            squares.insert(0, right_square)
            right -= 1

    return squares


if __name__ == "__main__":
    print(f"Squares: {make_squares([-2, -1, 0, 2, 3])}")
    print(f"Squares: {make_squares([-3, -1, 0, 1, 2])}")
    print(f"Squares: {make_squares([0, 1, 2, 4, 7, 9])}")
"""
Binary Search - Search a 2D Matrix II (medium)

Description:
Write an efficient algorithm that searches for a target value in an m x n 
integer matrix. The matrix has the following properties:
* Integers in each row are sorted in ascending from left to right.
* Integers in each column are sorted in ascending from top to bottom.

Example:
Input: 
matrix = [[1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]], 
target = 5

Output: true

LeetCode: 
https://leetcode-cn.com/problems/search-a-2d-matrix-ii
and 
https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
"""

def search_matrix(matrix: list, target: int) -> bool:
    """ Flag Number

    If we use brute force to search the matrix, the complexity will be O(M*N)
    where M and N are the number of rows and columns in the matrix.

    We can rotate the matrix by 45 degrees, and it becomes a graph which is 
    similar to binary search tree. For each element, the left branch is 
    smaller than it and the right branch is larger than it. We can start from 
    the root node (bottom-left or top-right), and search for the target.

    Suppose we use the bottom-left element as the mark / flag, then we can 
    compare the current element with the target:
    1. If flag > target, then target must be above flag, move the row upper 
    by 1. 
    2. If flag < target, then target must be at the right of current flag, 
    move the column right by 1.
    3. If flag == target, then we found the target, return True.

    Time Complexity - O(M+N) - M and N are the number of rows and columns.
    Space Complexity - O(1) - Constant space for variables.
    """
    # Edge cases
    if not matrix or not matrix[0]: return False

    rows, columns = len(matrix), len(matrix[0])
    i, j = rows - 1, 0

    while i >=0 and j <= columns - 1:
        element = matrix[i][j]
        if element > target:
            i -= 1
        elif element < target:
            j += 1
        else:
            return True
    
    return False


if __name__ == "__main__":
    matrix = [[1,4,7,11,15],
            [2,5,8,12,19],
            [3,6,9,16,22],
            [10,13,14,17,24],
            [18,21,23,26,30]] 
    target = 5
    print(search_matrix(matrix, target))
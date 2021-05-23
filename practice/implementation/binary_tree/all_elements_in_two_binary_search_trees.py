"""
BST - All Elements in Two Binary Search Trees (medium)

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in 
ascending order.

Example:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

LeetCode: 
https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/
"""
from tree_node import TreeNode, create_tree_from_list


def merge_bsts(root1: TreeNode, root2: TreeNode) -> list:
    """ Inorder Traversal + Merge Sort

    We can traverse the two tree with inorder and put the elements into two 
    lists, and according to the property of BST, the two lists are sorted. 
    We can then merge these two arrays with merge sort.

    Time Complexity - O(M + N) - M and N are the number of nodes in two trees. 
    The inorder traversal takes O(M + N), merge sorting also takes O(M + N), 
    so in total O(M + N).
    Space Complexity - O(M + N) - For the extra two arrays.
    """
    def inorder_traversal(root, nodes):
        """ Inorder traversal and append values into the list. """ 
        # Recursion termination
        if not root: return None

        inorder_traversal(root.left, nodes)
        nodes.append(root.val)
        inorder_traversal(root.right, nodes)
    
    # Traverse the two trees and get the sorted values.
    values1, values2 = [], []
    inorder_traversal(root1, values1)
    inorder_traversal(root2, values2)

    # Start merge sort using two pointers starting at index 0.
    res, i, j = [], 0, 0
    # Get the length of two arrays.
    m, n = len(values1), len(values2)
    while i < m and j < n:
        # Two cases to add values from values1:
        # 1. Array values2 is exhausted, only values1 remaining.
        # 2. values1[i] <= values2[j] while i < m and j <=n.
        if values1[i] <= values2[j]:
            res.append(values1[i])
            i += 1
        # The same for array values2.
        else:
            res.append(values2[j])
            j += 1
    # Add the remaining part of values1 or values2.
    res += values1[i:] + values2[j:]
    return res

if __name__ == "__main__":
    root1 = create_tree_from_list([2,1,4])
    root2 = create_tree_from_list([1,0,3])
    print(merge_bsts(root1, root2))

    root1 = create_tree_from_list([])
    root2 = create_tree_from_list([5,1,7,0,2])
    print(merge_bsts(root1, root2))
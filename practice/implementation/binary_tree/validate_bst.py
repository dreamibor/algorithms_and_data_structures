"""
Binary Search Tree - Validate Binary Search Tree (medium)

Description:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

Example:
Input: root = [2,1,3]
Output: true

LeetCode: https://leetcode-cn.com/problems/validate-binary-search-tree/
"""

from tree_node import TreeNode, create_tree_from_list


def validate_bst_in_order(root: TreeNode) -> bool:
    """ Traverse the BST with inorder and see if the result sequence is ascending.

    In pratice, we can compare the current node's value with the previous node and 
    see if it's larger than the previous node.

    Time Complexity - O(N) - Iterate the binary tree once.
    Space Complexity - O(N) - For saving the traversed nodes.
    """
    # Inorder traversal and put the result into list.
    def inorder(root, result):
        if root is None:
            return
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)
    
    result = []
    inorder(root, result)

    # Compare the current node and the next tree node to 
    # see if it's larger than the next node, if yes, then 
    # it's not binary search tree.
    for i in range(len(result) - 1):
        if result[i] >= result[i+1]:
            return False

    return True

def validate_bst_recursion(root: TreeNode) -> bool:
    """ Recursion - using the properties of BST.

    We can design a function helper(root, min, max) to recursivelt check if the root 
    node is in the range of (min, max). 

    When we are checking the left sub-tree, we shall change the max to root.val, since 
    all the values in the sub-tree shall be smaller than the root value. Also, when 
    checking the right tree, the min shall be changed to root.val.

    In the begining, we shall use helper(root, -inf, +inf).

    Time Complexity - O(N) - Recursively iterate the binary tree once.
    Space Complexity - O(N) - For the recursion stack.
    """

    def helper(node, min=float('-inf'), max=float('inf')) -> bool:
        # If we have reached the leaves.
        if not node:
            return True
        
        # Check if the root node value is in the (min, max) range
        if node.val <= min or node.val >= max:
            return False
        
        # Check the right node and change the min to root node's value.
        if not helper(node.right, node.val, max):
            return False
        
        # # Check the left node and change the max to root node's value.
        if not helper(node.left, min, node.val):
            return False
        
        return True

    return helper(root)


if __name__ == "__main__":
    root_arr = [5, 1, 4, None, None, 3, 6]
    root = create_tree_from_list(root_arr)
    print(validate_bst_in_order(root))
    print(validate_bst_recursion(root))

    root_arr = [2, 1, 3]
    root = create_tree_from_list(root_arr)
    print(validate_bst_in_order(root))
    print(validate_bst_recursion(root))
    
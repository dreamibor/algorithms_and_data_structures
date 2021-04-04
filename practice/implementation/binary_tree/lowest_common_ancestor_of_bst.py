"""
Binary Tree - Lowest Common Ancestor of a Binary Search Tree

Description:
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes 
in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined 
between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

Example:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

LeetCode: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""
from tree_node import TreeNode, create_tree_from_list


def lowest_common_ancestor_recursion(root, p, q) -> TreeNode:
    """ Recursion - using BST properties

    Since we are looking for p and q:
    1. If p and q are both larger than root, then the LCA is in the right sub-tree, 
    2. If p and q are both smaller than root, then the LCA is in the left sub-tree.
    3. p and q are in root's two sides respectively.
    
    """
    if p.val < root.val > q.val:
        return lowest_common_ancestor_recursion(root.left, p, q)
    if p.val > root.val < q.val:
        return lowest_common_ancestor_recursion(root.right, p, q)

    return root

def lowest_common_ancestor(root, p, q) -> TreeNode:
    """ Non-recursion - using BST properties

    The same idea as the recursion version, but just not using recursion.
    """
    while root:
        if p.val < root.val > q.val:
            root = root.left
        elif p.val > root.val < q.val:
            root = root.right
        else:
            return root


if __name__ == "__main__":
    root_arr = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root = create_tree_from_list(root_arr)
    p = root.left
    q = root.right
    # Recursion
    lca = lowest_common_ancestor_recursion(root, p, q)
    print(lca.val)
    # Non-recursion
    lca = lowest_common_ancestor(root, p, q)
    print(lca.val)
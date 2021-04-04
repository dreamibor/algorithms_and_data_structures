"""
Binary Tree - Lowest Common Ancestor of a Binary Tree

Description:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow 
a node to be a descendant of itself).”

Example:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

LeetCode: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
from tree_node import TreeNode, create_tree_from_list


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """ Recursion - Find P and Q.

    Ancestor - If p is in the (left or right) sub-tree of root, or p == root, then
    we call root is the ancestor of p.

    Lowest Common Ancestor (LCA) - there are some situations where root will be the 
    LCA of p and q:
    1. p and q are both in root's sub-tree and are in the left and right sub-tree 
    respectively. 
    2. p == root, and q is in root's left or right sub-tree.
    3. q == root, and p is in root's left or right sub-tree.

    Solution:
    We can traverse the binary tree recursively with postorder, return when we see 
    the node p or q, when p, q are on the two sides of root, then root will be LCA, 
    return root.
    
    Time Complexity - O(N) - Traverse the tree once.
    Space Complexity - O(N) - For recursion stack.
    """
    # Terminate condition:
    # 1. When we've gone beyond leaf nodes.
    # 2. When root is p or q, then return root.
    if not root or root == p or root == q:
        return root
    
    # Recusion - check left and right sub-tree.
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    """
    According to the value of left and right, there are four situations:
    1. When left and right are both None, meaning both root's left and right 
    sub-tree don't contain p or q, return None.
    2. When left and right are  not None, meaning p, q are in the two sides 
    of root, so root is the LCA, return root.
    3. When left is None, and right is not None, meaning p, q are not in the 
    left sub-tree, so return right.
    4. When right is None and left is not None, meaning p, q are not in the 
    right sub-tree, so return left.

    """
    # p,q don't exist in left sub-tree.
    if not left: return right
    # p,q don't exist in right sub-tree.
    if not right: return left

    return root # For left and right both exist.


if __name__ == "__main__":
    root_arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_tree_from_list(root_arr)
    p = root.left
    q = root.right
    lca = lowest_common_ancestor(root, p, q)
    print(lca.val)
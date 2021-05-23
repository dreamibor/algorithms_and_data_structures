"""
Backtracking - Longest Univalue Path (medium)

Description:
Given the root of a binary tree, return the length of the longest path, 
where each node in the path has the same value. This path may or may not 
pass through the root.

The length of the path between two nodes is represented by the number of 
edges between them.

Example:
Input: root = [5,4,5,1,1,5]
Output: 2

LeetCode: https://leetcode-cn.com/problems/longest-univalue-path/
"""
import sys
sys.path.append('../')
from binary_tree.tree_node import TreeNode, create_tree_from_list


def longest_univalue_path(root: TreeNode) -> int:
    """ DFS / Recursion

    Using DFS or recursion to track the longest univalue path that the left 
    or right sub-tree can provide and update the maximum number of edges 
    along the way.

    Time Complexity - O(N) - Each node is only processed once.
    Space Complexity - O(H) - H is the height of the tree, for the recursion 
    stack.
    """
    # Edge cases - empty tree.
    if not root: return 0

    def backtracking(root):
        """ The maximum number of univalue edges or the longest univalue path 
        the sub-trees of root can provide to the father node.
        """
        nonlocal max_len
        # Recursion termination - reached leaf node.
        if not root: return 0

        # Calculate the left and right sub-trees' longest path.
        left = backtracking(root.left)
        right = backtracking(root.right)

        # If left and right node's value is the same as root, then 
        # update left and right sub-trees' longest path. Plus one to 
        # count the root node (add 1 edge).
        if root.left:
            if root.left.val == root.val:
                left += 1
            # If the value between left node and root are not the same, then 
            # the maximum length will be 0, as they shall not connect.
            else:
                left = 0
        
        # Same as the left sub-tree.
        if root.right:
            if root.right.val == root.val:
                right += 1
            else:
                right = 0
        
        # Compare the current path's longest length with the global one.
        max_len = max(max_len, left + right)
        # Return the larger one, so it can construct a longer path with 
        # parent node.
        return max(left, right)

    # Variable to record the maximum number of edges of univalue.
    max_len = 0
    backtracking(root)
    return max_len


if __name__ == "__main__":
    root = create_tree_from_list([5,4,5,1,1,5])
    print(longest_univalue_path(root))
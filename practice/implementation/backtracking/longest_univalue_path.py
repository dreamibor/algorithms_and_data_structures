"""
Backtracking - Longest Univalue Path (medium)

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
from binary_tree.tree_node import TreeNode, create_tree_from_list, traverse_inorder


def longest_univalue_path(root: TreeNode) -> int:
    pass



if __name__ == "__main__":
    root = create_tree_from_list([5,4,5,1,1,5])
    print(longest_univalue_path(root))
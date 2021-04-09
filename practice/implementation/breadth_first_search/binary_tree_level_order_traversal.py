"""
BFS - Binary Tree Level Order Traversal

Description:
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

LeetCode: https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
"""
import sys
sys.path.append('../')

from binary_tree.tree_node import TreeNode, create_tree_from_list


def level_order_traversal(root: TreeNode) -> list:
    """ BFS - Batch Processing

    We 're still doing BFS, but need to know which level we are at. One way is 
    to use batch processing, where we process each level as a batch, iterating 
    all nodes in the current level.

    Time Complexity - O(N) - All elements are iterated once.
    Space Complexity - O(N) - For queue and result.
    """
    # Edge cases - empty tree.
    if not root: return []

    queue = []
    queue.append(root)
    result = []

    while queue:
        # Get the number of all the nodes in the current level.
        level_size = len(queue)
        current_level_result = []

        # Iterate all nodes in the current level.
        for _ in range(level_size):
            node = queue.pop(0)
            current_level_result.append(node.val)
            # Add all next level nodes into the queue.
            if node.left: queue.append(node.left) 
            if node.right: queue.append(node.right) 

        result.append(current_level_result)

    return result


def level_order_traversal_dfs(root: TreeNode) -> list:
    """ DFS - Recursion

    Traverse with DFS, and add the element to corresponding level's list.

    Time Complexity - O(N) - All elements are iterated once.
    Space Complexity - O(N) - For recursion stack and result.
    """
    def dfs_helper(root, level):
        # Recursion termination
        if not root: return

        # Add a new empty list for this level.
        if len(result) < level + 1:
            result.append([])
        
        # Append the node's value into current level's list.
        result[level].append(root.val)

        # Recursion for next level.
        dfs_helper(root.left, level + 1)
        dfs_helper(root.right, level + 1)
        
    # Edge cases - empty tree.
    if not root: return []

    result = []
    dfs_helper(root, 0)
    return result


if __name__ == "__main__":
    root = create_tree_from_list([3, 9, 20, None, None, 15, 7])
    # For BFS
    print(level_order_traversal(root))
    # For DFS
    print(level_order_traversal_dfs(root))

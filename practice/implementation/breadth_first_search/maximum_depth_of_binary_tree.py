"""
BFS / DFS - Maximum Depth of Binary Tree (easy)

Description:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the 
root node down to the farthest leaf node.

Example:
Input: root = [3, 9, 20, None, None, 15, 7]
Output: 3

LeetCode: https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
"""
import sys
sys.path.append("../")

from binary_tree.tree_node import TreeNode, create_tree_from_list


def max_depth_bfs(root: TreeNode) -> int:
    """ BFS - Traverse by Level Order.
    
    Time Complexity - O(N) - All nodes are traversed once.
    Space Complexity - O(N) - For the queue.
    """
    # For edge cases
    if not root: return 0

    max_depth = 0
    queue = []
    queue.append(root)

    while queue:
        # The number of nodes in the current level.
        level_size = len(queue)

        # Iterate the whole level.
        for _ in range(level_size):
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        max_depth += 1
    
    return max_depth

def max_depth_dfs(root: TreeNode) -> int:
    """ DFS - with Recursion

    Assuming the maximum depth of left and right sub-tree are l and r, then the maximum 
    depth of the tree will be max(l, r) + 1. We can get the maximum depth for left and 
    right sub-tree using the same way. In practice, we can calculate the maximum depth 
    of the left and right sub-tree recursively, and the recursion will terminate at empty 
    nodes.

    Time Complexity - O(N) - All nodes are traversed once.
    Space Complexity - O(H) - H is height of the binary tree. 
    """
    # Recursion termination
    if not root: return 0

    # Plus one since the current level shall be counted as well.
    return 1 + max(max_depth_dfs(root.left), max_depth_dfs(root.right))


if __name__ == "__main__":
    root = create_tree_from_list([3, 9, 20, None, None, 15, 7])
    print(max_depth_bfs(root))
    print(max_depth_dfs(root))

    root = TreeNode(0)
    print(max_depth_bfs(root))
    print(max_depth_dfs(root))
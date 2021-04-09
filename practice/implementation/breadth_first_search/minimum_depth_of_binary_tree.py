"""
BFS / DFS - Minimum Depth of Binary Tree (easy)

Description:
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root 
node down to the nearest leaf node.

Note: A leaf is a node with no children.


Example:
Input: root = [3,9,20,null,null,15,7]
Output: 2

LeetCode: https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
"""
import sys
sys.path.append("../")

from binary_tree.tree_node import TreeNode, traverse_preorder, create_tree_from_list


def min_depth_bfs(root: TreeNode) -> int:
    """ BFS - Return when we get the first leaf node.

    Time Complexity - O(N) - All nodes are traversed once.
    Space Complexity - O(N) - For the queue.
    """
    # Edge case - empty tree.
    if not root: return 0

    min_depth = 0
    queue = []
    queue.append(root)

    while queue:
        # Get the numder of nodes in this level.
        level_size = len(queue)

        # Traverse through all nodes in this level.
        for _ in range(level_size):
            node = queue.pop(0)

            # Whenenver the node is a leaf node, return min depth.
            if not node.left and not node.right: return min_depth + 1
            # Add children into the queue.
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        min_depth += 1
    
    return min_depth

def min_depth_dfs(root: TreeNode) -> int:
    """ DFS - with Recursion.

    For each non-leaf node, to calculate the minimum depth, we only have to calculate 
    the minimum depth of it's left and right sub-trees.

    Time Complexity - O(N) - All nodes are traversed once.
    Space Complexity - O(H) - H is the height of the tree, where in the worst case, the 
    tree is just like a linked list, and the space complexity will be O(N). In average, 
    the space complexity shall be O(logN) for binary tree.
    """
    # Recursion termination
    if not root: return 0

    # For nodes that don't have either left or right sub-tree.
    if not root.left: return 1 + min_depth_dfs(root.right)
    if not root.right: return 1 + min_depth_dfs(root.left) 
    
    # Divide and Conquer
    return 1 + min(min_depth_dfs(root.left), min_depth_dfs(root.right))


if __name__ == "__main__":
    root = create_tree_from_list([3, 9, 20, None, None, 15, 7])
    print(min_depth_bfs(root))
    print(min_depth_dfs(root))

    root = create_tree_from_list([2, None, 3, None, None, None, 4,None,None, None, None, None, None, None, 5, None, 
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, 6])
    print(min_depth_bfs(root))
    print(min_depth_dfs(root))
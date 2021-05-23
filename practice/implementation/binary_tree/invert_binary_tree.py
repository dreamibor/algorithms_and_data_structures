"""
Recursion - Invert Binary Tree (easy)

Description:
Given the root of a binary tree, invert the tree, and return its root.

Example:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

LeetCode: https://leetcode-cn.com/problems/invert-binary-tree/
"""
from tree_node import TreeNode, create_tree_from_list, traverse_inorder


def invert_tree(root: TreeNode) -> TreeNode:
    """ Recursion

    Traverse the tree recursively from root node to leaf nodes, and start 
    inverting from the leaf nodes. If the left and right sub-trees have been 
    inverted, then we just need to swap the position of these two sub-trees.

    Time Complexity - O(N) - Iterate all the nodes only once.
    Space Complexity - O(N) - For the recursion stack, equals to the height 
    of the binary tree, usually it's O(logN), the worst case will be O(N) as 
    the tree has become a linked list.
    """
    # Recursion termination.
    if not root: return root

    # Invert left and right sub-tree recursively.
    left = invert_tree(root.left)
    right = invert_tree(root.right)
    # Swap left and right sub-tree position.
    root.left, root.right = right, left

    return root

def invert_tree_bfs(root: TreeNode) -> TreeNode:
    """ BFS / Iteration with Queue.

    We can also traverse the tree with BFS using queue. We first swap the 
    left and right sub-tree of the current node, and add the swapped left and 
    right sub-trees into the queue for future traversal.  

    Time Complexity - O(N) - Iterate all the nodes only once.
    Space Complexity - O(N) - For the recursion stack, equals to the height 
    of the binary tree, usually it's O(logN), the worst case will be O(N) as 
    the tree has become a linked list.
    """
    if not root: return root

    # Queue for BFS 
    queue = [root]

    while queue:
        temp = queue.pop(0)
        # Swap current node's left and right sub-trees.
        temp.left, temp.right = temp.right, temp.left

        # Add left sub-tree into queue if it's non-empty.
        if temp.left: queue.append(temp.left)
        
        # Add right sub-tree into queue if it's non-empty.
        if temp.right: queue.append(temp.right)
    
    return root

if __name__ == "__main__":
    root = create_tree_from_list([4,2,7,1,3,6,9])
    new_root = invert_tree(root)
    print("First test case: ")
    traverse_inorder(new_root)
    new_root = invert_tree_bfs(root)
    traverse_inorder(new_root)

    root = create_tree_from_list([2,1,3])
    new_root = invert_tree(root)
    print("Second test case: ")
    traverse_inorder(new_root)
    new_root = invert_tree_bfs(root)
    traverse_inorder(new_root)

    root = create_tree_from_list([])
    new_root = invert_tree(root)
    print("Third test case: ")
    traverse_inorder(new_root)
    new_root = invert_tree_bfs(root)
    traverse_inorder(new_root)
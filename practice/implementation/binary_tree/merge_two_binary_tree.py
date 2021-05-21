"""
DFS / BFS - Merge Two Binary Trees (easy)

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the 
two trees are overlapped while the others are not. You need to merge the two 
trees into a new binary tree. The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. Otherwise, the 
NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

LeetCode: https://leetcode-cn.com/problems/merge-two-binary-trees/
"""
from tree_node import TreeNode, create_tree_from_list, traverse_inorder


def merge_two_trees_dfs(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """ DFS / Recursion

    We can traverse the two trees from root node at the same time using DFS, 
    and merge corresponding nodes. There are three cases:
    1. Both of the two nodes are empty, then the merged one will be empty as 
    well.
    2. If there is only one node is empty, then the non-empty node will be 
    the merged node.
    3. If both nodes are non-empty, then we shall calculate the sum of the 
    two nodes' values to merge them. 

    Time Complexity - O(min(M, N)) - M, N are the number of nodes for the 
    two trees. 
    Space Complexity - O(1) - If operating on the original tree such as 
    root1, then it's constant, otherwise, O(min(M,N)). 
    """
    # Edge cases, rooot1 or root2 is None.
    if not root1: return root2
    if not root2: return root1

    # Otherwise, root1 and root2 both exist, update the value and dive into 
    # left and right node. After the two edge cases, it's equivalent to 
    # if root1 and root2:
    root1.val += root2.val
    root1.left = merge_two_trees_dfs(root1.left, root2.left)
    root1.right = merge_two_trees_dfs(root1.right, root2.right)
    
    return root1


def merge_two_trees_bfs(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """ BFS / Iteration

    We can traverse the two trees with BFS as well. Also, we can implement 
    iteration with stack for the previous recursion version.

    As long as the two left nodes are not empty, we put them into the queue, 
    also, the same for right nodes. We take them from the queue and sum them 
    together (to tree1).

    If the left node of root1 is empty but not root2, then we can just assign 
    the left node of root2 to root1. The same happens to right node cases.

    Time Complexity - O(min(M, N)) - M, N are the number of nodes for the 
    two trees. 
    Space Complexity - O(min(M, N)) - We need extra space for the queue. 
    """
    # Edge cases - one of the tree is empty.
    if not root1: return root2
    if not root2: return root1

    queue = [(root1, root2)]

    while queue:
        # Take nodes both exist in two trees.
        r1, r2 = queue.pop(0)
        r1.val += r2.val

        # For the left node of root1 and root2, if they are both not empty, 
        # then put them into the queue.
        if r1.left and r2.left:
            queue.append((r1.left, r2.left))
        # Otherwise, if root1's left node is empty, assign root2 to root1.
        # Ignored root2's node is empty here as we are assign values to root1.
        elif not r1.left:
            r1.left = r2.left
        
        # The same for right nodes.
        if r1.right and r2.right:
            queue.append((r1.right, r2.right))
        elif not r1.right:
            r1.right = r2.right

    return root1

if __name__ == "__main__":
    root1 = create_tree_from_list([1,3,2,5])
    root2 = create_tree_from_list([2,1,3,None,4,None,7])
    print("DFS: ")
    traverse_inorder(merge_two_trees_dfs(root1, root2))
    
    root1 = create_tree_from_list([1,3,2,5])
    root2 = create_tree_from_list([2,1,3,None,4,None,7])
    print("BFS: ")
    traverse_inorder(merge_two_trees_bfs(root1, root2))


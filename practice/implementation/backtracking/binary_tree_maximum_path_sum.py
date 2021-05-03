"""
DFS - Binary Tree Maximum Path Sum (hard)

Description:
A path in a binary tree is a sequence of nodes where each pair of adjacent 
nodes in the sequence has an edge connecting them. A node can only appear 
in the sequence at most once. Note that the path does not need to pass 
through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

Example:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 
2 + 1 + 3 = 6.

LeetCode: https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
"""
import sys
sys.path.append('../')
from binary_tree.tree_node import TreeNode, create_tree_from_list


def max_path_sum(tree: TreeNode) -> int:
    """ Recursion

    Meaning of the problem:
    1. For the path, we can start at any node and arrive at any node (可以
    从任意节点出发, 到达任意节点).
    2. The path shall contain at least one node, and it doesn't need to pass 
    the root node.
    3. Get the maximum path sum of all possible paths.

    Reference:
    https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/
    shou-hui-tu-jie-hen-you-ya-de-yi-dao-dfsti-by-hyj8/

    Time Complexity - O(N) - N is the number of nodes in the tree, each node
    will be traversed at most twice.
    Space Complexity - O(N) - For the recursion call stack, which equals to 
    the maximum depth of the binary tree.
    """
    def helper(node: TreeNode):
        """ 
        The helper function is used to calculate the maximum contribution 
        (gain) value of the current node, meaning the maximum path sum the 
        current sub-tree can provide to it's father node. 

        There are three cases:
        1. The path stop at the current sub-tree's root node, then the gain 
        is root.val.
        2. Going deeper to the left sub-tree, then the maximum gain is: 
        root.val + helper(root.left).
        3. Going deeper to the right sub-tree, then the maximum gain is: 
        root.val + helper(root.right).

        So, to the farther node, the maximum gain of this sub-tree is:
        root.val + max(helper(root.left) + helper(root.right))
        We shall return this value for each sub-tree's root node.

        Also, the path with maximum path sum could exist in a local sub-tree. 
        So for each sub-tree, we shall calculate the maximum path sum for it 
        and compare it with the global maximum path sum and update accordingly.

        A sub-tree's local maximum path sum is: 
        helper(root.left) + root.val + helper(root.right).
        """
        # Recursion termination, when the node is None, return 0.
        nonlocal max_sum
        if not node: return 0

        # To make the sum as larger as possible, we shall drop the values
        # (set to 0), if the sub-tree's gain contribution is negative.
        left_gain = max(helper(node.left), 0)
        right_gain = max(helper(node.right), 0)

        # Calculate the local sub-tree's maximum path sum and compare it 
        # with the global maximum path sum.
        local_subtree_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, local_subtree_sum)

        # Return the maximum path sum the root node can provide to it's 
        # father node.
        return node.val + max(left_gain, right_gain)
    
    # Global maximum path sum
    max_sum = float("-inf")
    helper(tree)
    return max_sum


if __name__ == "__main__":
    nodes = [1,2,3]
    tree = create_tree_from_list(nodes)
    print(max_path_sum(tree))

    nodes = [-10,9,20,None,None,15,7]
    tree = create_tree_from_list(nodes)
    print(max_path_sum(tree))
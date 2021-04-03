"""
Define binary tree node and helper functions.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree_from_list(arr: list) -> TreeNode:
    """ Create a binary tree from the input list.

    For a given node at index `i` the children of that node are (2*i)+1 for left child 
    and (2*i)+2 for right child. Python use this technique to model a heap.
    """
    def insert_nodes_level_order(arr: list, root: TreeNode, i: int, n: int):
        if i < n:
            # Ignore tree node with None value
            if arr[i] is None:
                return
            
            temp = TreeNode(arr[i])
            root = temp

            # Insert the left and rught child.
            root.left = insert_nodes_level_order(arr, root.left, 2 * i + 1, n)
            root.right = insert_nodes_level_order(arr, root.right, 2 * i + 2, n)
        
        return root

    root = None
    return insert_nodes_level_order(arr, root, 0, len(arr))

def traverse_inorder(root):
    """ Traverse the tree with in order (root node in the middle).
    """
    if root is None:
        return
    traverse_inorder(root.left)
    print(root.val)
    traverse_inorder(root.right)

def traverse_preorder(root: TreeNode):
    """ Traverse the tree with in order (access root node first).
    """
    if root is None:
        return
    print(root.val)
    traverse_preorder(root.left)
    traverse_preorder(root.right)

def traverse_postorder(root: TreeNode):
    """ Traverse the tree with in order (root node at last).
    """
    if root is None:
        return
    traverse_postorder(root.left)
    traverse_postorder(root.right)
    print(root.val)

if __name__ == "__main__":
    arr = [5, 1, 4, None, None, 3, 6]
    root = create_tree_from_list(arr)
    # Preorder
    print("Preorder traverse: ")
    traverse_preorder(root)
    # Inorder
    print("Inorder traverse: ")
    traverse_inorder(root)
    # Postorder
    print("Postorder traverse: ")
    traverse_postorder(root)
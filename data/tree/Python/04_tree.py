from __future__ import print_function

class Node(object):
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.data)


# Traversal Tree Node in in, pre and post order.
def print_tree_preorder(tree):
    if tree == None: return
    print(tree.data)
    print_tree_preorder(tree.left)
    print_tree_preorder(tree.right)

def print_tree_inorder(tree):
    if tree == None: return
    print_tree_inorder(tree.left)
    print(tree.data)
    print_tree_inorder(tree.right)

def print_tree_postorder(tree):
    if tree == None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.data)

if __name__ == '__main__':
    tree = Node('+', Node(1), Node('*', Node(2), Node(3)))
    print(print_tree_inorder(tree))

class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, value):
        if value <= self.data:
            if self.left == None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if value == self.data:
            return True
        if value < self.data:
            if self.left == None:
                return False
            else:
                return self.left.find(value)
        else:
            if self.right == None:
                return False
            else:
                return self.right.find(value)

    def print_in_order(self):
        if self.left != None:
            self.left.print_in_order()
        print(self.data)
        if self.right != None:
            self.right.print_in_order()

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
    
def check_BST(root, min, max):
    if root == None:
        return True
    if root.data < min or root.data > max:
        return False
    return check_BST(root.left, min, root.data) and check_BST(root.right, root.data, max)

        
tree = TreeNode(5,TreeNode(3),TreeNode(8))
tree.insert(6)
tree.insert(0)
tree.insert(4)
print(tree.find(3))
tree.print_in_order()
print(check_BST(tree, -200, 200))
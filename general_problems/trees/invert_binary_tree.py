def invertBinaryTree(tree):
    # Write your code here.
    if not tree:
        return tree
    invertBinaryTree(tree.right)
    invertBinaryTree(tree.left)
    tree.right, tree.left = tree.left, tree.right


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameterHelper(tree, cur_path):
    if not tree:
        return cur_path
    return max(1 + cur_path, max(
        binaryTreeDiameterHelper(tree.right), 
        binaryTreeDiameterHelper(tree.left)))

def binaryTreeDiameter(tree):
    # Write your code here.
    if not tree:
        return 0 

    return binaryTreeDiameterHelper(tree, 0)


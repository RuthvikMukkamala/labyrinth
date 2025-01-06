def nodeDepthsHelper(root, level):
    if not root:
        return 0
    newLevel = level + 1
    return level + nodeDepthsHelper(root.right, newLevel) + nodeDepthsHelper(root.left, newLevel)

def nodeDepths(root):
    # Write your code here.
    if not root:
        return 0

    return nodeDepthsHelper(root.right, 1) + nodeDepthsHelper(root.left, 1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

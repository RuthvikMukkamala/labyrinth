# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def evaluateExpressionTree(tree):
    # Write your code here.
    if not tree:
        return 0

    return evaulateExpressionTreeHelper(tree)



def evaulateExpressionTreeHelper(tree):
    if tree.value >= 0:
        return tree.value

    if tree.value == -1:
        return evaulateExpressionTreeHelper(tree.left) + evaulateExpressionTreeHelper(tree.right)
    if tree.value == -2:
        return evaulateExpressionTreeHelper(tree.left) - evaulateExpressionTreeHelper(tree.right)
    if tree.value == -3:
        return int(evaulateExpressionTreeHelper(tree.left) / evaulateExpressionTreeHelper(tree.right)) 
    if tree.value == -4:
        return evaulateExpressionTreeHelper(tree.left) * evaulateExpressionTreeHelper(tree.right)


    return -1
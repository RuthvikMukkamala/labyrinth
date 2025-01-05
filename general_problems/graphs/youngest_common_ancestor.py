# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    ancestoral_set = set()

    while descendantOne and descendantOne.name:
        ancestoral_set.add(descendantOne)
        descendantOne = descendantOne.ancestor

    while descendantTwo and descendantTwo.name:
        if descendantTwo in ancestoral_set:
            return descendantTwo
        descendantTwo = descendantTwo.ancestor

    return None



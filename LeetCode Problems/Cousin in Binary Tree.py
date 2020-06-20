'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.
'''

# Definition for a binary tree root.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root, x, y):

        dx = self.getDepth(root, x)
        dy = self.getDepth(root, y)

        px = self.getParent(root, x)
        py = self.getParent(root, y)

        return dx == dy and px != py

    def getParent(self, root, val):
        '''
        inputs: the root and the target node's value
        returns: the value of the parent of the target node
        '''

        if root is None or root.val == val:  # base case, return to previous layer
            return None

        if (root.left is not None and root.left.val == val) or (root.right is not None and root.right.val == val):
            # if current node's left or right is the target node, current node is the parent node. return its value
            return root.val
        else:
            parent = self.getParent(root.left, val)  # current node is not parent, try its left node
            if parent is not None:  # parent node found in left branch
                return parent
    
            parent = self.getParent(root.right, val) # parent node NOT found in left branch, try the right branch
            if parent is not None:
                return parent


    def getDepth(self, root, val):
        if root is None:  # empty node (very bottom of a branch)
            return None

        depth = 0

        if root.val == val: # target node found
            return depth + 1
        else:
            depth = self.getDepth(root.left, val)
            if depth is not None:
                return depth + 1

            depth = self.getDepth(root.right, val)
            if depth is not None:
                return depth + 1

        return depth

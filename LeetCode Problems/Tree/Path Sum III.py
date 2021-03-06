'''
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
      root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

            10
           /  \
          5   -3
         / \    \
        3   2   11
       / \   \
      3  -2   1

      Return 3. The paths that sum to 8 are:

      1.  5 -> 3
      2.  5 -> 2 -> 1
      3. -3 -> 11
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, sum):
        self.nPath = 0
        self.sum = sum
        self.traverse(root)
        return self.nPath
    
    def traverse(self, node):
        if not node:
            return
        self.checkSum(node, self.sum) # check if there is a path that passes through current node
        self.traverse(node.left)
        self.traverse(node.right)
        
    def checkSum(self, node, remain): 
        if not node:
            return
        if remain - node.val == 0:
            self.nPath += 1
        if node.left:
            self.checkSum(node.left, remain-node.val)
        if node.right:
            self.checkSum(node.right, remain-node.val)

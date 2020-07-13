'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        self.isSumFound = False # if root is None, return False
        self.checkSum(root, sum)
        return self.isSumFound
    
    def checkSum(self, node, remain):
        if not node: 
            return
        
        if not node.left and not node.right:  # leaf node
            if remain - node.val == 0: # sum found
                self.isSumFound = True
        if node.left:
            self.checkSum(node.left, remain-node.val)
        if node.right:
            self.checkSum(node.right, remain-node.val)

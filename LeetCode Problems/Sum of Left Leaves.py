'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        self.leftSum = 0
        self.traverse(root, False)
        return self.leftSum
    
    def traverse(self, node, isLeftNode):
        if not node:
            return
        
        if not node.left and not node.right and isLeftNode: # leaf node
            self.leftSum += node.val
        
        self.traverse(node.left, True)
        self.traverse(node.right, False)
            

'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, sum):
        res = []
        self.dfs(res, root, sum, [])
        return res
    
    def dfs(self, res, node, remain, subset):
        if node:
            if (not node.left) and (not node.right) and remain-node.val == 0: # reached leaf node and sum 
                res.append(subset+[node.val])

            if node.left:
                self.dfs(res, node.left, remain-node.val, subset+[node.val])
            if node.right:
                self.dfs(res, node.right, remain-node.val, subset+[node.val])

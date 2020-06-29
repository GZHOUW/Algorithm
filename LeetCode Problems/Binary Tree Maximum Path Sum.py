'''
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

Example 1:
  Input: [1,2,3]

         1
        / \
       2   3
  Output: 6

Example 2:
  Input: [-10,9,20,null,null,15,7]
     -10
     / \
    9  20
      /  \
     15   7
  Output: 42
'''

class Solution:
    def maxPathSum(self, root):
        if not root:
            return 0
        self.res = -float(inf) # the max path sum found so far
        self.postOrder(root)
        return self.res
    
    def postOrder(self, node):
        if not node:
            return 0
        left = max(self.postOrder(node.left), 0) # the return value of left branches, if negative, set to zero(dont use nodes that sum to negative value)
        right = max(self.postOrder(node.right), 0) # the return value of right branches
        
        # update res if larger path sum is found
        self.res = max(self.res, left + right + node.val)
        
        # return value is NOT max path sum
        # returns the larger of (cur + all left) path and (cur + all right) path
        return max(left, right) + node.val
        

'''
Given a binary tree, find the length of the longest path where each node in the path has the same value. 
This path may or may not pass through the root.
The length of path between two nodes is represented by the number of edges between them.
 
Example 1:
    Input:

                  5
                 / \
                4   5
               / \   \
              1   1   5
    Output: 2

Example 2:
    Input:

                  1
                 / \
                4   5
               / \   \
              4   4   5
    Output: 2
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.maxLen = 0
        self.traverse(root, None)        
        return self.maxLen
    
    def traverse(self, node, parentVal):
        if not node:
            return 0
        
        left= self.traverse(node.left, node.val) # the longest Univalue Path in left branch
        right = self.traverse(node.right, node.val)  # the longest Univalue Path in right branch
        self.maxLen = max(self.maxLen, left + right)
        print(node.val)
        if node.val == parentVal:
            return 1 + max(left, right) # add one to left or right
        else:
            return 0

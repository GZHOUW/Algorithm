'''
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:
  Input:

     1
   /   \
  2     3
   \
    5

  Output: ["1->2->5", "1->3"]

  Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root):
        self.res = []
        self.traverse(root, "")
        return self.res
    
    def traverse(self, node, path):
        if not node:
            return
        path += str(node.val)
        if not node.left and not node.right:
            self.res.append(path)
        if node.left:
            self.traverse(node.left, path + '->')
        if node.right:
            self.traverse(node.right, path + '->')

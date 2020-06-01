'''
Invert a binary tree.

Example:

Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root
    
    def traverse(self, node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.traverse(node.left)
        self.traverse(node.right)
        

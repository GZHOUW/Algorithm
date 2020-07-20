'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example:
    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    return its minimum depth = 2.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):
        # empty root
        if not root:
            return 0
        
        # leaf(no branch) node
        if not root.left and not root.right:
            return 1
        
        # one branch node, need to keep going down the other way
        if not root.left: 
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left) 
        
        # two branch node, check both branches
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

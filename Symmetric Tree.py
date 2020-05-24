'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 
But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
   
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, l, r):
        if not l and not r:
            return True
        elif not l or not r:
            return False
        
        if l.val != r.val:
            return False
        
        # mirror --> node.left.left = node.right.right, node.left.right = node.right.left
        return self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left) 
        

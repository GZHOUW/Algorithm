'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
    Given tree s:

         3
        / \
       4   5
      / \
     1   2
    Given tree t:
       4 
      / \
     1   2
    Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
    Given tree s:

         3
        / \
       4   5
      / \
     1   2
        /
       0
    Given tree t:
       4
      / \
     1   2
    Return false.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, s, t):
        if not s:
            return
        if self.isEqual(s,t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        return False
    
    def isEqual(self, t1, t2):
        if not t1 and not t2:
            return True
        elif not t1 or not t2:
            return False
        
        if t1.val != t2.val:
            return False
        else:   
            return self.isEqual(t1.left, t2.left) and self.isEqual(t1.right, t2.right)

'''
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
    Input: 
      Tree 1:                     Tree 2:                  
              1                         2                             
             / \                       / \                            
            3   2                     1   3                        
           /                           \   \                      
          5                             4   7                  
    Output: 
    Merged tree:
           3
          / \
         4   5
        / \   \ 
       5   4   7
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left

        self.right = right
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if not t1 and not t2:
            return None
        elif not t1: # t1 is None, t2 is not None
            return t2
        elif not t2: # t2 is None, t1 is not None
            return t1
        
        t3 = TreeNode(t1.val + t2.val) # merged tree
        t3.left = self.mergeTrees(t1.left, t2.left)
        t3.right = self.mergeTrees(t1.right, t2.right)
        
        return t3
        
    def mergeTreesStack(self, t1, t2):
        if t1 is None: 
            return t2
        stack = [(t1,t2)]
        
        while stack:
            n1, n2 = stack.pop()
            if n2 is None: # No need to change anything
                continue
            n1.val += n2.val # add n2 value to n1
            
            if n1.left is None: 
                n1.left = n2.left # copy entire node in order to copy the child nodes of n2.left
            else: 
                stack.append((n1.left, n2.left))
            
            if n1.right is None: 
                n1.right = n2.right
            else: 
                stack.append((n1.right, n2.right))
        return t1

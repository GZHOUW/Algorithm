'''
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]
Output: false
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pVal = []
        qVal = []
        
        self.traverse(p, pVal)
        self.traverse(q, qVal)
        return pVal == qVal
    
    def traverse(self, node, valList):
        if node is None:
            valList.append(None)
            return
        valList.append(node.val)
        self.traverse(node.left, valList)
        self.traverse(node.right, valList)
        

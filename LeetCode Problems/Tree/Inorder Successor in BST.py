'''
Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.
If the given node has no in-order successor in the tree, return null.

Example 1:
    Input: {1,#,2}, node with value 1
    Output: 2
    Explanation:
      1
       \
        2
    
Example 2:
    Input: {2,1,3}, node with value 1
    Output: 2
    Explanation: 
        2
       / \
      1   3

Challenge
    O(h), where h is the height of the BST.

Notice
    It's guaranteed p is one node in the given tree. (You can directly compare the memory address to find p)
'''

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here

        res = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                res = root
                root = root.left
        
        return res
    


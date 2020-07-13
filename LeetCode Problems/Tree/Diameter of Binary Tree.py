'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
Note: The length of path between two nodes is represented by the number of edges between them.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        self.d = 0 # number of links along the diameter
        self.height(root)
        return self.d
    
    def height(self, node):
        if node == None: # this line is not run until the very left bottom node is reached
            return 0 # at very bottom, both L and R are set to 0
        # preorder traversal, left before right
        lHeight = self.height(node.left)
        rHeight = self.height(node.right)
        
        # this line is not run until the very left bottom node is reached
        self.d = max(self.d, lHeight + rHeight)  # get current diameter (sum of L and R at a node), and compare with largest known diameter
        return max(lHeight, rHeight) + 1 # go to previous lavel, and add 1 to L or R

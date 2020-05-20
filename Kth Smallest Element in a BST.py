'''
iven a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # in a BST, left node < root < right node, therefore, 
        # inorder traversal of BST is an array sorted in the ascending order.
        
        inOrderNodes = []
        
        self.inOrderTraverse(root, inOrderNodes)
        return inOrderNodes[k-1] # the k th element from the end (k th smallest)
    
    def inOrderTraverse(self, node, inOrderNodes):
        if not node:
            return
        self.inOrderTraverse(node.left, inOrderNodes)
        inOrderNodes.append(node.val)
        self.inOrderTraverse(node.right, inOrderNodes)

'''
Given a binary tree, return the preorder traversal of its nodes' values.

pre-order traversal:
1. visit root
2. go to left sub-tree
3. visit the entire left sub-tree with pre-order traversal
4. go to right sub-tree
5. visit the entire right sub-tree with pre-order traversal

pseudo code:
def preorder(node):
    if node == None:
        return
    print(node)
    preorder(node.left)
    preorder(node.right)
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def preorderTraversal(self, root):# recursion method
        self.nodes = []
        self.traverse(root)
        return self.nodes
    
    def traverse(self, node):
        if node == None:
            return # go back to previous level
        self.nodes.append(node.val)
        self.traverse(node.left)
        self.traverse(node.right)
        
'''iteration method:

    def preorderTraversal(self, root):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
'''

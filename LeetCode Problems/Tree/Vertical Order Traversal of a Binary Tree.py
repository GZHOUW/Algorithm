# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Algorithm:  1. Create a dict that stores nodes based on x coordinates
            2. Traverse the tree recursively and complete the dict
            3. sort the dict by x value and then sort every dict[x] by y value
            4. Append to res list
'''
class Solution:
    def verticalTraversal(self, root):
        dict = {}# key = x-coordinate, val = (y-coordinate, node.val)
        res = []
        self.traverse(root, 0, 0, dict)
        
        for x in sorted (dict.keys()): # sort dict by x value
            temp = []
            for (y, node_val) in sorted(dict[x]): # sort the node list by y value
                temp.append(node_val)
            res.append(temp)
        return res
    
    def traverse(self, node, x, y, dict):
        if not node:
            return
        if x in dict:
            dict[x].append((y, node.val))
        else:
            dict[x] = [(y, node.val)]
        
        self.traverse(node.left, x-1, y+1, dict)
        self.traverse(node.right, x+1, y+1, dict)
            
        
        

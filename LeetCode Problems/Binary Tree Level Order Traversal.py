# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root):
        if not root: 
            return []
        queue = deque([root]) # deque is basically a list that supports adding and removing elements from either end
        res = []
        
        while queue:
            curLevelVals = [] # stores the values of current level, reset to [] every level
            size = len(queue)
            for i in range(size):
                curNode = queue.popleft()
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                curLevelVals.append(curNode.val)  # fill curLevelVal with the left and right children of cur level nodes
            res.append(curLevelVals)
            
        return res

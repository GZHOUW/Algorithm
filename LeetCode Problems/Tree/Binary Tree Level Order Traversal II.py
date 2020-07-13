'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root):
        if not root: 
            return []
        # deque is basically a list that supports adding and removing elements from either end
        queue = deque([root]) # the first level must have only one node (root)
        allLevelVals = []
        
        while queue:
            curLevelVals = [] # stores the values of current level, reset to [] every level
            size = len(queue)
            for i in range(size):
                # pop all current level elements from queue, and append all next level elements to the queue
                curNode = queue.popleft()
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                    
                # fill curLevelVal with the left and right children of cur level nodes
                curLevelVals.append(curNode.val)  
            allLevelVals.append(curLevelVals)
            
        return allLevelVals[::-1]

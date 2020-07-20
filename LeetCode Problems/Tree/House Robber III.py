'''
After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
    Input: [3,2,3,null,3,null,1]

         3
        / \
       2   3
        \   \ 
         3   1

    Output: 7 
    Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
    Input: [3,4,5,1,3,null,1]

         3
        / \
       4   5
      / \   \ 
     1   3   1

    Output: 9
    Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution():
    def rob(self, root):
        self.map = {}
        return self.rob2(root)
    
    def rob2(self, root):
        if not root:
            return 0
        
        if root in self.map:
            return self.map[root]
    
        val1 = root.val # the amount can be obtained by robbing this level and the next next level
        if root.left:
            val1 += self.rob2(root.left.left) + self.rob2(root.left.right)
        if root.right:
            val1 += self.rob2(root.right.left) + self.rob2(root.right.right)
        
        val2 = self.rob2(root.left) + self.rob2(root.right) # the amount can be obtained by robbing the next level 
        max_val = max(val1, val2) # the better choice
        
        
        self.map[root] = max_val
        return max_val

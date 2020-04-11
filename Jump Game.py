'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''

def canJump(nums):
    end = len(nums) - 1
    max_reach = 0
    for i, step in enumerate(nums):
        if max_reach >= end: # max reach is/exceeds the end
            return True
        elif max_reach < i: # max_reach stayed at i-1, cannot reach current index i
            return False
        max_reach = max(max_reach, i + step)

'''
Demo:
index         0 1 2 3 4 5 6 7 8
list         [3,0,3,2,0,0,1,2,1]
max_reach     3 3 5 5 5 5 F-------> 5 < 6
'''

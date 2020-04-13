'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''

def findMaxLength(nums):
    '''
    Demo: [1,0,0,1]
    idx = -1 ------> count =  0
    idx =  0 ------> count =  1
    idx =  1 ------> count =  0
    idx =  2 ------> count = -1
    idx =  3 ------> count =  0

    find the largest difference between two idx with same count:
    3 - (-1) = 4
    '''
    
    count = 0
    countDict = dict()
    countDict[count] = -1  # the initial "index" need to be -1, because when idx=0, count becomes -1 or 1
    length = []
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1

        if count not in countDict:
            countDict[count] = i # new count value, add to dict
        else: # back at same count, should record
            length.append(i - countDict[count])# the largest difference between two idx with same count is the answer
    if length:
        return max(length)
    else: # all 1 or all 0
        return 0

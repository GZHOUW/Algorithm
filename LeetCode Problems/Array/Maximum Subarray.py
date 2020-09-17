'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# dynamic programming
def maxSubArray(nums):
    ''' Demo
    [0, 1, -3, 4, -1, 2, 1, -5, 4]
    [0, 1, -2, 4,  3, 5, 6,  1, 5]
       new    new       max

    '''
    dp = [nums[0]] # Each element is the sum of current subarray
    res = nums[0]
    for i in range(1, len(nums)):
        if dp[i - 1] <= 0: # If the previous sum is negative or 0, break that subarray, start a new one
            dp.append(nums[i])
        else:
            dp.append(nums[i] + dp[i - 1]) # add nums[i] to current subArray
        res = max(res, dp[i]) # update result
    return res

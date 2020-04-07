'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# dynamic programming
def maxSubArray(nums):
    # if all elements are positive, maxSubArray is entire list
    # if all elements are negative, maxSubArray is the max number
    dp = [nums[0]]
    res = nums[0]
    for i in range(1, len(nums)):
        if dp[i - 1] < 0: # dp[i - 1] is the sum of current subArray
            dp.append(nums[i]) # start a new subArray, discard the previous
        else:
            dp.append(nums[i] + dp[i - 1]) # add nums[i] to current subArray
        res = max(res, dp[i]) # update result
    return res

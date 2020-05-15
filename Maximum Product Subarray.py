'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

def maxProduct(nums);
    max_prod = nums[0]  # maximum product calculated so far (likely positive)
    min_prod = nums[0]  # minimum product calculated so far (likely negative)
    res = nums[0]
    for i in range(1, len(nums)):       
        # max product can be created by either multiplying by previous max product, previous min prodoct, or 1 (do nothing)
        max_prod,  min_prod   =   max(nums[i], max_prod*nums[i], min_prod*nums[i]),   min(nums[i], max_prod*nums[i], min_prod*nums[i]) 
        '''
        x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
        y = min(nums[i], max_prod*nums[i], min_prod*nums[i])            
        max_prod, min_prod = x, y
        '''
        res = max(res, max_prod)  # update res
    return res

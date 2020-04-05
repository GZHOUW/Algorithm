"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

type nums: List[int]
type target: int
rtype: int
"""

def threeSumClosest(self, nums, target):
    nums.sort() # sort the array so that binary search can be used
    length = len(nums)

    diff = abs(target - (nums[0] + nums[1] + nums[2]))
    res = nums[0] + nums[1] + nums[2]

    for a in range(length):
        b = a + 1 # one after a
        c = length - 1 # last
        while b < c:
            sum_i = nums[a] + nums[b] + nums[c] # current sum
            diff_i = abs(target - sum_i) # diff between target and current sum
            if diff_i < diff: # smaller diff --> closer to target
                diff = diff_i
                res = sum_i   
            if sum_i == target: # 
                return sum_i
            elif sum_i < target: # binary search
                b += 1
            else: # sum_i > target
                c -= 1
    return res

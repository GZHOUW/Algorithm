"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

type nums: List[int]
type target: int
rtype: List[int]

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        
        complementDict = {} # hash table: key = complement, item = index
        for i in range(len(nums)):  
            complement = target - nums[i]
            if nums[i] in complementDict: # look for key that is equal to ith element
                return [complementDict[nums[i]], i] # return index (item of dict)
            else:
                complementDict[complement] = i # add key to dict

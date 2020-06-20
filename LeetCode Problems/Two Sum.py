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

def twoSum(nums, target):
    compDict = {} # hash table: key = complement, item = index
    for i in range(len(nums)):  
        num_i = nums[i]
        complement = target - num_i
        if num_i in compDict: # if the complement of the ith element is already in compDict
            return [compDict[num_i], i] # return index (item of dict)
        else:
            compDict[complement] = i # add key to dict

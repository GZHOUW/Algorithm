'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''

class Solution:
    '''
    Demo: nums = [1,1,1,2], target = 3
    [1] first 1
    [1,1] first 1 and second 1
    [1,1,1] append, return to [1,1]
    [1,1,2] fail, return to [1,1]
    ignore third 1
    [1,2] append, return
    '''

    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        self.getCombSum(candidates, target, res, 0, [])
        return res

    def getCombSum(self, nums, target, res, startIdx, subset):
        if target < 0:  # subset does NOT add to target
            return # return to previous layer
        if target == 0:  # subset DOES add to target
            res.append(subset) # add to solution
            return # return to previous layer
        for i in range(startIdx, len(nums)):
            if i > startIdx and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self.getCombSum(nums, target-nums[i], res, i+1, subset+[nums[i]])
            '''
            nums = candidates
            target = target - nums[i]: subtract current number from target, if target gets to 0, return solution
            res = [existing solution subsets]
            startIdx = i + 1: one element only could be used once
            subset = subset + [nums[i]]: add current number to subset
            '''

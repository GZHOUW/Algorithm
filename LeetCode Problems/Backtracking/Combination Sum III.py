'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution:
    def combinationSum3(self, k, n):
        res = []
        nums = [1,2,3,4,5,6,7,8,9]
        self.findComb(k, n, res, nums, 0, [])
        return res
    
    def findComb(self, limit, target, res, nums, start, subset):
        if target < 0:
            return
        if len(subset) == limit and target == 0:
            res.append(subset)
            return
        for i in range(start, len(nums)):
            if nums[i] > target:
                break
            self.findComb(limit, target-nums[i], res, nums, i+1, subset+[nums[i]])

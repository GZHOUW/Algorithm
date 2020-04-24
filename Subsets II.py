'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        self.nums = nums
        self.res = []
        self.getSubsets(0, [])
        return self.res
        
    def getSubsets(self, index, subset):
        if subset not in self.res:
            self.res.append(subset)
        for i in range(index, len(self.nums)):
            self.getSubsets(i + 1, subset + [self.nums[i]])
    

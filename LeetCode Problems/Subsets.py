'''
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

def subsets(nums):
    solSet = [[]]
    for num in nums:
        new = []
        for subset in solSet:
            new.append(subset + [num]) # 1. new = [[1]]; 2. new = [[2], [1,2]]
        solSet += new # 1. solSet = [[], [1]]; 2. solSet = [[], [1], [2], [1,2]]
    return solSet

# Recursive Method
def subsetsR(self, nums):
    self.nums = nums
    self.res = [] # contains all subsets, gets updates every recursion layer
    self.getSubset(0, []) # start with the entire list (idx=0) and initial subset []
    print(self.res)
    return self.res

def getSubset(self, index, subset):
    # index: start from 0, +1 every layer of recursion
    self.res.append(subset)
    for i in range(index, len(self.nums)): # loop in the remaining nums
        self.getSubset(i+1, subset+[self.nums[i]]) # index += 1

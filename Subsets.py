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
def subsetsR(nums):
      res = []
      getSubset(nums, 0, [], res)
      return res

def getSubsetR(nums, index, subset, res):
    '''
    nums: original list, doesn't change
    index: start from 0, +1 every layer of recursion
    res: contains all subsets, gets updates every recursion layer
    '''
    res.append(subset)
    for i in range(index, len(nums)):
        getSubset(nums, i+1, subset+[nums[i]], res) # add the current num to each existing subset

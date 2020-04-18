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

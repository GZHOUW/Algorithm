'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution:
    def combinationSum(self, candidates, target):
        self.res = []
        self.nums = candidates
        self.dfs(target, 0, [])
        return self.res

    def dfs(self, target, index, subset):
        if target < 0:
            return # back to previous layer
        if target == 0:
            self.res.append(subset) # sum in the subset is target
            return # back to previous layer
        for i in range(index, len(self.nums)):
            self.dfs(target - self.nums[i], i, subset + [self.nums[i]])
            '''
            target - nums[i]: subtract current number from target, if target gets to 0, return solution
            subset + [nums[i]]: add current number to subset
            '''


a = Solution()
l = [2, 3, 6, 7]
print(a.combinationSum(l, 7))

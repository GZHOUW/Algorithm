'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.getComb(res, n, k, 1, [])
        return res
    
    def getComb(self, res, n, length, start, subset):
        if len(subset) == length:
            res.append(subset)
        for i in range(start, n+1):  # i = 1,2,3,4
            new_subset = subset + [i]
            self.getComb(res, n, length, i+1, new_subset)


'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
class Solution():
    '''
    Algorithm: create in-place dp where dp[r][c] is the min path to arrive at grid[r][c]
    '''
    def minPathSum(self, grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 and c!= 0:
                    grid[r][c] = grid[r][c] + grid[r][c-1]
                elif r != 0 and c == 0:
                    grid[r][c] = grid[r][c] + grid[r-1][c]
                elif r!= 0 and c!=0:
                    grid[r][c] = min(grid[r-1][c], grid[r][c-1]) + grid[r][c]
        return grid[-1][-1]


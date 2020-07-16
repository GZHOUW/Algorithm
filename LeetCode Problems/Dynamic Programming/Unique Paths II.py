'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid: # edge case
        return 0
    row = len(obstacleGrid)
    col = len(obstacleGrid[0])

    # Create a new matrix with same dimention with all 1
    # Because start node is 1
    resMat = []
    for i in range(row):
        resMat.append([])
        for j in range(col):
            resMat[i].append(1)

    for r in range(row):
        for c in range(col):
            if obstacleGrid[r][c] == 1: # obatacle
                resMat[r][c] = 0 # no way to get to an obstacle
            else:
                if r == 0 and c == 0: #start node
                    continue
                elif r == 0:
                    resMat[r][c] = resMat[r][c-1]
                elif c == 0:
                    resMat[r][c] = resMat[r-1][c]
                else:
                    resMat[r][c] = resMat[r][c-1] + resMat[r-1][c] 

    return resMat[-1][-1] # Return number of paths for the last grid (finish)

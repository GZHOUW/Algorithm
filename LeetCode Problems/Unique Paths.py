'''
A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?
'''

def uniquePaths(c, r):

    # Edge Cases
    if c == 0 or r == 0:
        return 0
    elif c == 1 or r == 1:
        return 1

    # Create a new matrix with same dimention with all 1
    # Because row 1 and column 1 are all 1
    resMat = []
    for i in range(r):
        resMat.append([])
        for j in range(c):
            resMat[i].append(1)

    for a in range(1, r):
        for b in range(1, c):
            # the number of unique paths for reaching any grid is 
            # the number in left grid plus the number in the above grid
            resMat[a][b] = resMat[a][b-1] + resMat[a-1][b] 

    return resMat[-1][-1] # Return number of paths for the last grid (finish

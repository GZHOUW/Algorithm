'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:
    Input:
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]
    Output: 16
'''

class Solution:
    def islandPerimeter(self, grid):
        self.perimeter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    self.countPerimeter(grid,r,c)
        return self.perimeter
    
    def countPerimeter(self, grid, r, c):
        for x,y in ((r+1,c), (r-1, c), (r, c+1), (r, c-1)):
            if x<0 or y<0 or x== len(grid) or y==len(grid[0]) or grid[x][y] == 0:
                self.perimeter += 1

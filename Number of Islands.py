'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
'''

class Solution():

    def countIslands(self, grid):
        self.grid = grid
        if len(self.grid) == 0:  # edge case: no element
            return 0

        r = len(self.grid)
        c = len(self.grid[0])

        if r == 1 and c == 1:  # edge case: one element
            return str(self.grid[r][c])

        count = 0
        for i in range(r):
            for j in range(c):
                if self.grid[i][j] == "1": # when encounter 1, add count, change the "island" to 0
                    count += 1
                    self.sinkIsland(i, j)
        return count

    def sinkIsland(self, i, j):
        neighbors = self.getNeighbors(i, j) # get the adjacent 1s to the current 1

        if not neighbors: # when there are no more adjacent 1
            return

        for idx in neighbors:  # [(0, 2), (0, 0)]
            self.grid[idx[0]][idx[1]] = "0"  # change current 1 to 0
            self.sinkIsland(idx[0], idx[1]) # sink the rest of island



    def getNeighbors(self, i, j):
        neighbors = []
        for idx in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:  # up, right, down, left
            if idx[0] >=0 and idx[0] < len(self.grid) and idx[1] >= 0 and idx[1] < len(self.grid[0]) and self.grid[idx[0]][idx[1]] == "1":
                neighbors.append(idx)
        return neighbors

grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]

a = Solution()
print(a.countIslands(grid))

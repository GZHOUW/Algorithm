'''
Description

You are given a m x n 2D grid initialized with these three possible values
    -1: A wall or an obstacle.
    0: A gate.
    INF: Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF

Example1
    Input:
    INF  -1  0  INF
    INF INF INF  -1
    INF  -1 INF  -1
     0  - 1 INF INF

    the answer is:
    3  -1   0   1
    2   2   1  -1
    1  -1   2  -1
    0  -1   3   4
'''

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    self.dfs(rooms, r, c, 1)


    def dfs(self, rooms, r, c, distance):
        for x,y in ((r+1,c), (r, c+1), (r-1, c), (r, c-1)):
            if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]) and rooms[x][y] > distance: # check for valid and shorter than existing distance
                rooms[x][y] = distance
                self.dfs(rooms, x, y, distance+1)

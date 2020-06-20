'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

class Solution:
    def totalNQueens(self, n):
        self.nSolution = 0
        self.queenPos = [-1] * n
        self.placeQueen(0)

        return self.nSolution
    
    def placeQueen(self, r): # Backtracking 
        if r == len(self.queenPos):
            self.nSolution += 1
            return
        for c in range(len(self.queenPos)):
            if self.isValid(r,c):
                self.queenPos[r] = c
                self.placeQueen(r+1) # go to the next row
        self.queenPos[r] = -1
        return
    
    def isValid(self, r, c):
        for rPrev, cPrev in enumerate(self.queenPos[0:r]):
            if cPrev == c or c-r == cPrev-rPrev or c+r == cPrev+rPrev:
                return False
        return True

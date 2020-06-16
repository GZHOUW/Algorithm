'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

  Input: 4
  Output: [
   [".Q..",  // Solution 1
    "...Q",
    "Q...",
    "..Q."],

   ["..Q.",  // Solution 2
    "Q...",
    "...Q",
    ".Q.."]
  ]
  Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''

class Solution:
    def solveNQueens(self, n):
        res_board = []
        self.res = []
        self.queenPos = [-1] * n
        self.placeQueen(0)
        
        # Format the output
        for i in range(len(self.res)):
            board_i = [['.' for __ in range(n)] for _ in range(n)]
            for r in range(n):
                c = self.res[i][r]
                board_i[r][c] = 'Q'
                board_i[r] = "".join(board_i[r])
            res_board.append(board_i[:])
        return res_board
    
    def placeQueen(self, r): # Backtracking 
        if r == len(self.queenPos):
            self.res.append(self.queenPos[:])
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

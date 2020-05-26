'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
'''

class Solution:
    def solve(self, board):
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r == 0 or r == len(board)-1 or c == 0 or c == len(board[0])-1) and board[r][c] == 'O':
                    self.capture(board, r, c)
        
        # Change all 'O's to 'X'. Change 'E's back to 'O'
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'E':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
    
    def capture(self, board, r, c):
        board[r][c] = 'E'
        for x,y in ((r+1,c), (r, c+1), (r-1, c), (r, c-1)):
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O':
                board[x][y] = 'E' # Set the 'O's that are on the edge or connected to edge to 'E'
                self.capture(board, x, y)
                

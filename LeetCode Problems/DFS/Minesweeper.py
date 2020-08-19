'''
You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.
Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
'''

class Solution:
    def updateBoard(self, board, click:):
        # update board to final state
        r = click[0]
        c = click[1]
        if board[r][c] == 'M':
            board[r][c] = 'X'
        elif board[r][c] == 'E':
            self.sweepAndUpdate(board, r, c)
        
        return board
    
    def sweepAndUpdate(self, board, r, c):
        num_mines = 0
        adjacent = ((r-1,c),(r-1,c-1),(r-1,c+1),(r,c-1),(r,c+1),(r+1,c+1),(r+1,c),(r+1,c-1))
        
        # sweep, find the number of mines in adjacent cells
        for x,y in adjacent:
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'M':
                num_mines += 1
        
        # update the current cell based on number of mines
        if num_mines == 0:
            board[r][c] = 'B'
            for x,y in adjacent:
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'E':
                    self.sweepAndUpdate(board, x, y)
        else:
            board[r][c] = str(num_mines)
            return

'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

class Solution:
    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:  # found the first char, start search
                    if self.search(board, r, c, word):
                        return True
        return False
    
    def search(self, board, r, c, substring):
        if len(substring) == 0:
            return True
        #                 out of board                                         wrong char
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != substring[0]:
            return False
        
        board[r][c] = None  # Delete used char to avoid using same char twice
        
        # Perform recursive search in 4 directions
        if self.search(board, r-1, c, substring[1:]): # ABCD --> BCD --> CD --> D
            return True
        if self.search(board, r+1, c, substring[1:]):
            return True
        if self.search(board, r, c-1, substring[1:]):
            return True
        if self.search(board, r, c+1, substring[1:]):
            return True
        
        board[r][c] = substring[0]  # if not found, restore the board and return to rpev level
        return False
                

'''
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

Example:
    Input: 
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]

    Output: ["eat","oath"]
'''

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()    

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        s = self.root
        for char in word:
            if char not in s:  # new branch
                s[char] = dict()
                s = s[char]
            else: # the letter exists in this layer, go to next layer and check next char
                s = s[char]
        
        # After loop ends, a word has been inserted, mark the end of this word
        s["isWordEnd"] = True

class Solution:
    def findWords(self, board, words):
        trie = Trie()
        self.res = []
        for word in words:
            trie.insert(word)
        t = trie.root
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in t:
                    self.dfs(board, r, c, t, "")
        return list(set(self.res))
    
    def dfs(self, board, r, c, t, curStr):
        cur = board[r][c]
        if cur not in t:
            return
        else:
            if "isWordEnd" in t[cur]:
                self.res.append(curStr+cur)
            board[r][c] = 'X' # only use once
            for x,y in ((r+1,c),(r-1, c), (r, c+1), (r, c-1)):
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    self.dfs(board, x, y, t[cur], curStr+cur)
            board[r][c] = cur

'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

class Solution:
    def maximalSquare(self, matrix):
        if not matrix: 
            return 0
        
        row = len(matrix)
        col = len(matrix[0])
        lenMat = [[0 for _ in range(col+1)] for __ in range(row+1)]
        # lenMat[r][c] denotes the length of edge of the square which matrix[r-1][c-1] is is bottom right corner of the square
        # e.g. lenMat[1][1] corresponds to matrix[0][0]
        max_edge = 0 # length of the edge of the largest square
        
        for r in range(1, row+1):
            for c in range(1, col+1):
                if matrix[r-1][c-1] == "1": # cur element is 1
                    # if left, upper left, and up are all one, it is a complete square matrix with all ones
                    # e.g. if lenMat[r-1][c-1], lenMat[r-1][c], lenMat[r][c-1] are all 1, this means:
                    #  1 1 1 
                    #  1 1 1
                    #  1 1 c --> the up, left, and upper-left are all bottom right corner of a square (2x2), therefore cur forms a new square, add one to length
                    lenMat[r][c] = min(lenMat[r-1][c-1], lenMat[r-1][c], lenMat[r][c-1]) + 1
                max_edge = max(max_edge, lenMat[r][c])
        return max_edge * max_edge
    

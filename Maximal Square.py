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

def maximalSquare(matrix):
    if not matrix: 
        return 0

    row = len(matrix)
    col = len(matrix[0])
    lenMat = []
    for i in range(row+1): # same size as matrix, all 0
        lenMat.append([])
        for _ in range(col+1):
            lenMat[i].append(0)
    length = 0

    for r in range(1, row+1):
        for c in range(1, col+1):
            if matrix[r-1][c-1] == "1":
                # if left, upper left, and up are all one, it is a complete square matrix with all ones
                lenMat[r][c] = min(lenMat[r-1][c-1], lenMat[r-1][c], lenMat[r][c-1]) + 1
            length = max(length, lenMat[r][c])
    return length *length

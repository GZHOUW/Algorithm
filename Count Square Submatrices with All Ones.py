'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
'''

def countSquares(self, matrix: List[List[int]]) -> int:
    '''
    Demo:

    matrix = [[0,1,1,1],
             [1,1,1,1],
             [0,1,1,1]]


        dummy col
    count = [[0,0,0,0,0], dummy row
             [0,0,1,1,1],
             [0,1,1,2,2],
             [0,0,1,2,3]]
    '''
    res = 0
    count = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 1:  # current cell must be 1 to complete any square
                # count[r+1][c+1] stores the number of squares with count[r+1][c+1] as the bottom right corner
                count[r+1][c+1] = min(count[r][c+1], count[r+1][c], count[r][c]) + 1 # add one becasue current is one (at least add one square)
                res += count[r+1][c+1]
    return res

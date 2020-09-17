'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

def generateMatrix(n):
    matrix = [[0 for _ in range(n)] for __ in range(n)] # empty matrix
    rStart = 0
    rEnd = n - 1
    cStart = 0
    cEnd = n - 1
    num = 1  # number to be added, start with 1

    while rStart <= rEnd and cStart <= cEnd:
        for j in range(cStart, cEnd+1): # top row
            matrix[rStart][j] = num
            num += 1
        rStart += 1

        for i in range(rStart, rEnd+1): # right col
            matrix[i][cEnd] = num
            num += 1
        cEnd -= 1

        if rStart <= rEnd:
            for j in range(cEnd, cStart-1, -1): # bottom row
                matrix[rEnd][j] = num
                num += 1
        rEnd -= 1

        if cStart <= cEnd:
            for i in range(rEnd, rStart-1, -1): # left col
                matrix[i][cStart] = num
                num += 1
        cStart += 1

    return matrix

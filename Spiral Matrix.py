'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    res = []
    if len(matrix) == 0:
        return res

    rStart = 0
    rEnd = len(matrix) - 1
    cStart = 0
    cEnd = len(matrix[0]) - 1

    while rStart <= rEnd and cStart <= cEnd:
        for j in range(cStart, cEnd+1):
            res.append(matrix[rStart][j])
        rStart += 1

        for i in range(rStart, rEnd+1):
            res.append(matrix[i][cEnd])
        cEnd -= 1

        if rStart <= rEnd:
            for j in range(cEnd, cStart-1, -1):
                res.append(matrix[rEnd][j])
        rEnd -= 1

        if cStart <= cEnd:
            for i in range(rEnd, rStart-1, -1):
                res.append(matrix[i][cStart])
        cStart += 1

    return res

    ''' Break Algorithm 
    while True:
        if len(matrix) == 0: break

        for n in matrix.pop(0): # top row
            elements.append(n)
        if len(matrix) == 0: break

        for row in matrix: # right colomn
            elements.append(row.pop())
        if len(matrix[0]) == 0: break

        for n in matrix.pop()[::-1]: # bot row
            elements.append(n)
        if len(matrix) == 0: break

        for row in matrix[::-1]: # left column
            elements.append(row.pop(0))
        if len(matrix[0]) == 0: break

    return elements
    '''

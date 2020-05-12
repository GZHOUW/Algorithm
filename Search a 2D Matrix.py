'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    rStart = 0
    rEnd = len(matrix) - 1
    rTarget = None
    while rStart <= rEnd:
        rMid = (rEnd - rStart)//2 + rStart
        if  matrix[rMid][0] <= target <= matrix[rMid][-1]:
            rTarget = rMid
            break
        elif target < matrix[rMid][0]:
            rEnd = rMid - 1
        else:
            rStart = rMid + 1

    if rTarget is None:
        return False

    cStart = 0
    cEnd = len(matrix[0])
    while cStart <= cEnd:
        cMid = (cEnd - cStart)//2 + cStart
        if matrix[rTarget][cMid] == target:
            return True
        elif target < matrix[rTarget][cMid]:
            cEnd = cMid - 1
        else:
            cStart = cMid + 1

    return False


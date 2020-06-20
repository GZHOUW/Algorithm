'''
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.
'''


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n_row = binaryMatrix.dimensions()[0]
        self.n_col = binaryMatrix.dimensions()[1]
        res = self.n_col  # return leftmost column index(0-indexed) with at least a 1 in it.

        for r in range(n_row):
            firstOne = self.findFirstOne(binaryMatrix, r)
            if firstOne < res:
                res = firstOne
        
        if res == self.n_col:
            return -1
        else:
            return res
                    
    
    def findFirstOne(self, matrix, r):
        start = 0
        end = self.n_col - 1 # 3
        while start <= end:
            mid = (end - start) // 2 + start
            cur = matrix.get(r, mid)
            
            if cur == 1:
                if mid == 0 or matrix.get(r, mid - 1) == 0:
                    return mid
                else:
                    end = mid - 1
            elif cur == 0:
                start = mid + 1
        return self.n_col

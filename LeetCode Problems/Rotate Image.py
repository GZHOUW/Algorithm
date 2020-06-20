'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
rotate the image in-place, modify the input 2D matrix directly. DO NOT allocate another 2D matrix.
'''

def rotate(matrix):
    '''
    reverse the matrix vertically, and then find its transpose
    1 2 3     7 8 9     7 4 1
    4 5 6  => 4 5 6  => 8 5 2
    7 8 9     1 2 3     9 6 3
    ''' 
    matrix.reverse() # reverse vertically
    for i in range(len(matrix)): # find transpose
        for j in range(len(matrix[0])):
            if j > i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

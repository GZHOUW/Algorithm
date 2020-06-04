'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

class Solution:
    def numTrees(self, n):
        '''
        Demo: numBST[4] = numBST[3] + numBST[1]*numBST[2] + numBST[2]*numBST[1] + numBST[3]
                          root = 1        root = 2              root = 3          root = 4
                           3 right     1 left 2 right        2 left 1 right      3 left
        '''
        numBST = [0 for _ in range(n+1)] # stores number of unique BSTs when n = index
        numBST[0] = 1 # empty tree
        numBST[1] = 1 # only a root

        for i in range(2, len(numBST)):
            for j in range(i): 
                numBST[i] += numBST[j] * numBST[i-1-j] # i = 3,    j = 0         j = 1        j = 2
                                                       #         +=T[2]T[0]   +=T[1]T[1]   +=T[0]T[2] 
                                                       #         (i-1-j)(j)    (i-1-j)(j)   (i-1-j)(j)

        return numBST[n]

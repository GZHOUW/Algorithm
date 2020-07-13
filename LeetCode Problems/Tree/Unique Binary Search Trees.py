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
        numBST = [0 for _ in range(n+1)] # stores number of unique BSTs when n = index
        numBST[0] = 1 # empty tree
        numBST[1] = 1 # only a root

        for i in range(2, len(numBST)):
            for j in range(i+1): 
                '''
                let j be the root, there can be j-1 nodes on the left of root, and i-j nodes on the right
                e.g. i = 3, j = 2,  (j-1)=1 on left, (i-j) = 1 on right
                numBST[j-1] and numBST[i-j] represents the number of possible combinations of BSTs can be constructed by j-1 and i-j nodes respectively
                Multiply because: Say there are L number of possible unique BSTs on the left side of root and R on the right, 
                then each possibility of L can correspond to each possibility of R, therefore the total possibility (combination) would be L*R
                '''
                numBST[i] += numBST[j-1] * numBST[i-j]

        return numBST[n]

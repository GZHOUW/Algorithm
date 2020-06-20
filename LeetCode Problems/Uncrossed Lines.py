'''
Same as 1143. Longest Common Subsequence

We write the integers of A and B (in the order they are given) on two separate horizontal lines.
Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.
Return the maximum number of connecting lines we can draw in this way.

Example 1:
  Input: A = [1,4,2], B = [1,2,4]
  Output: 2
  Explanation: We can draw 2 uncrossed lines as in the diagram.
  We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

Example 2:
  Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
  Output: 3

Example 3:
  Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
  Output: 2
'''

class Solution:
    def maxUncrossedLines(self, A, B):
        # Add dummy element at beginning of A and B to represent empty list
        A = [None] + A
        B = [None] + B
        
        # dp[i][j] denotes the max number of lines can be drawn with i elements of A and j elements of B
        # i = 0 and j = 0 represents 0 elements in A and B (empty list), therefore the first row and col of dp must all be 0
        dp = [[0 for _ in B] for __ in A]
        
        for i in range(1, len(dp)): # A[i] corresponds to dp[i] because of dummy added
            for j in range(1, len(dp[0])):
                if A[i] == B[j]: # one line drawn between i and j
                    dp[i][j] = dp[i-1][j-1] + 1 # i+1 and j+1 will also contain this line
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # either same as top or left
                    # EX: A=[1,2], B=[1] ----> same as A=[1],B=[1] ([i-1][j])
        return dp[-1][-1]

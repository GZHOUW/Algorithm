'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

class Solution:
    def numSquares(self, n):
        nSquare = [x for x in range(n+1)] # nSquare[i] stores the least number of PSNs which sum to i
    
        for i in range(2, len(nSquare)):  # 0 and 1 are base cases
            # try subtracking PSNs from cur number, find the PSN that is as large as possible without making remain negative
            for j in range(1, i):
                PSN = j * j 
                remain = i - PSN  # one perfect square number used, count into result
                if remain < 0:
                    break
                else:
                    nSquare[i] = min(nSquare[i], nSquare[remain] + 1) 
                    
        return nSquare[n]  # last element corresponds to n

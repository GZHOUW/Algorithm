'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
Space complexity should be O(n).

Example 1:
  Input: 2
  Output: [0,1,1]

Example 2:
  Input: 5
  Output: [0,1,1,2,1,2]
'''

class Solution:
    def countBits(self, num):
        '''
        Index : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        num :   0 1 1 2 1 2 2 3 1 2  2  3  2  3  3  4
        
        dp[0] = 0;          dp[0] = 0;
        dp[1] = dp[0] + 1;  dp[1] = dp[1-1] + 1;
        dp[2] = dp[0] + 1;  dp[2] = dp[2-2] + 1;
        dp[3] = dp[1] + 1;  dp[3] = dp[3-2] +1;
        dp[4] = dp[0] + 1;  dp[4] = dp[4-4] + 1;
        dp[5] = dp[1] + 1;  dp[5] = dp[5-4] + 1;
        dp[6] = dp[2] + 1;  dp[6] = dp[6-4] + 1;
        dp[7] = dp[3] + 1;  dp[7] = dp[7-4] + 1;
        dp[8] = dp[0] + 1;  dp[8] = dp[8-8] + 1;
        '''
        res = [0 for _ in range(num+1)]
        offset = 1
        
        for i in range(1, num+1):
            if offset * 2 == i:
                offset *= 2
        
            res[i] = res[i - offset] + 1
        return res

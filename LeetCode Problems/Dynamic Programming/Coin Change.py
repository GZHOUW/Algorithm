'''
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
    Input: coins = [1, 2, 5], amount = 11
    Output: 3 
    Explanation: 11 = 5 + 5 + 1

Example 2:
    Input: coins = [2], amount = 3
    Output: -1
'''

class Solution:
    def coinChange(self, coins, amount)
        dp = [float('inf')] * (amount+1) # dp[i] is the fewest number of coins that can make up amount i
        dp[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0: # a $5 coin cannot make up amount $3
                    dp[i] = min(dp[i], dp[i-coin] + 1) # dp[i-coin] is the fewest number of coins that makes up cur_amount-coin
                    # becasue the amount i-coin plus coin equals cur amount
                    ''' i.e. i=5, coins = [1,2,5]
                    coin = 1 ---> dp[i] = min(inf, dp[4] + 1)
                    coin = 2 ---> dp[i] = min(dp[i], dp[3]+1)
                    coin = 5 ---> dp[i] = min(dp[i], dp[0]+1)'''
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
        

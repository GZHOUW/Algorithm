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
        

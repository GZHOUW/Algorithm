'''
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

Example 1:
  Input: amount = 5, coins = [1, 2, 5]
  Output: 4
  Explanation: there are four ways to make up the amount:
  5=5
  5=2+2+1
  5=2+1+1+1
  5=1+1+1+1+1
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        Demo: 5, [1,2,5]
        initial: [1,0,0,0,0,0]
        i=1 -->  [1,1,1,1,1,1]
        i=2 -->  [1,1,2,2,3,3]
        i=5 -->  [1,1,2,2,3,4]
        '''
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]
    
    '''Recursive Soultion (LTE)
        self.combination = 0
        self.countComb(coins, amount, 0)
        return self.combination
    
    def countComb(self, coins, amount, index):
        if amount < 0:
            return
        if amount == 0:
            self.combination += 1
            return
        
        for i in range(index, len(coins)):
            self.countComb(coins, amount-coins[i], i)
            '''

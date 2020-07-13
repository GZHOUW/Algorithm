'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                 Total amount you can rob = 1 + 3 = 4.
Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
                 Total amount you can rob = 2 + 9 + 1 = 12.
'''

class Solution:
    def rob(self, nums[int]):
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums)+1)] # dp[i] stores the max profit at the ith house
        dp[0] = 0 # 0th house (doesnt exist)
        dp[1] = nums[0] # first house
        for i in range(2, len(dp)):
            '''
            robber has two choices: 1.rob cur house 2. not rob cur house
            1 --> its better to rob cur house than to rob prev house, add cur house value to cur-2 (prev of prev)
            2 --> its better to rob prev house than cur house, keep prev house
            '''
            dp[i] = max(dp[i-2]+nums[i-1], dp[i-1]) # nums[i-1] --> cur house
        return dp[-1]

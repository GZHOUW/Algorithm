'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
Si % Sj = 0 or Sj % Si = 0.
If there are multiple solutions, return any subset is fine.

Example 1:
  Input: [1,2,3]
  Output: [1,2] (of course, [1,3] will also be ok)

Example 2:
  Input: [1,2,4,8]
  Output: [1,2,4,8]
'''

def largestDivisibleSubset(nums):
    if not nums:
        return None
    # DP solution
    nums.sort() # if a%b=0, b%c=0, then a%c=0
    dp = [[num] for num in nums] # subsets[i] is the largest subset where the biggest number is equal to nums[i]

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j])+1:
                # i is always greater than j    if new subset would be longer than current subset(dp[i])
                dp[i] = dp[j] + [nums[i]] # add current number to dp[j]
    return max(dp, key=len)

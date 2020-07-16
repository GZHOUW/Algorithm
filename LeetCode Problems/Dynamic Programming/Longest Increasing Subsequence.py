'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
  Input: [10,9,2,5,3,7,101,18]
  Output: 4 
  Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
  
Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n log n) time complexity?

https://segmentfault.com/a/1190000003819886 Algorithm Explaination
'''

class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        maxLen = 0
        tails = [None for _ in nums]
        tails[0] = nums[0]
        
        for i in range(len(nums)):
            if nums[i] < tails[0]: # smaller than all tails, update the first tail
                tails[0] = nums[i]
            elif nums[i] > tails[maxLen]: # larger than all tails, create a longer LSI
                tails[maxLen+1] = nums[i]
                maxLen += 1
            else: # if in between, update the LSI that has tail that is just greater than nums[i]
                # perform binary search to find which LSI in tails to update
                left = 0
                right = maxLen
                target = nums[i]
                found = False
                while left <= right:
                    mid = (right-left)//2 + left
                    if tails[mid] == target:
                        found = True
                        break
                    elif tails[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                
                if found:
                    tails[mid] = nums[i]
                else:
                    tails[left] = nums[i]
        return maxLen + 1
    
    

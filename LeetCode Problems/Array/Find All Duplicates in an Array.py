'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [2,3]
'''

class Solution:
    '''
    Algorithm: 1. If cur num not in correct position, swap it to the correct position
               2. If the swap destination has the same number as cur, duplicate found
               
    '''
    def findDuplicates(self, nums): # Time = O(N), Space = O(1)
        res = set() 
        i = 0
        while i < len(nums):
            if nums[i] != i+1: # not in correct position, i.e. 1 at idx=2
                if nums[i] == nums[nums[i]-1]: # duplicate found, move on
                    res.add(nums[i])
                    i += 1
                else: # keep swapping until cur is either duplicate or right position
                    # swap
                    temp = nums[nums[i] - 1]
                    nums[nums[i] - 1] = nums[i]
                    nums[i] = temp
            else:
                i += 1
        return list(res)

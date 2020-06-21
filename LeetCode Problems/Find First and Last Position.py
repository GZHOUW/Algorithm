'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length == 0:
            return [-1, -1]  
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)
        return [first, last]
    
    
    
    def findFirst(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l+1  < r:
            mid = (r - l)//2 + l
            if nums[mid] < target:
                l = mid
            else:
                r = mid
                
        if nums[l] == target: # must check left first
            return l
        if nums[r] == target:
            return r
        
        return -1
    
    
    def findLast(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l+1  < r:
            mid = (r - l)//2 + l
            if nums[mid] > target:
                r = mid
            else:
                l = mid
        
        if nums[r] == target: # must check right first
            return r
        if nums[l] == target:
            return l
        return -1
            

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.

Example 1:
    Input: [1,3,5]
    Output: 1

Example 2:
    Input: [2,2,2,0,1]
    Output: 0
'''

class Solution:
    def findMin(self, nums):
        left= 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            '''
            1: mid is smaller than right
            2. if mid and right are in the same part, then nums[mid] < nums[right]
            3. if mid and right are in differnet parts, then nums[mid] > nums[right]
            '''
            if nums[mid] > nums[right]: # mid is in left segment, right is in right segment
                left = mid + 1
            
            elif nums[mid] < nums[right]: # mid and right are in same segment, can be either left or right
                right = mid
            
            else: # when nums[mid] and nums[right] are same (duplicate)
                right-= 1

        return nums[left]

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''

class Solution:
    def findMin(self, nums):
        if not nums:
            return None

        left = 0
        right = len(nums)-1
        '''
        [3,1,2]
        mid=1 --> go left --> left=0,right=0
        mid=0 --> go right --> left=1, right=0
        '''
        while left <= right:
            mid = (right-left)//2 + left
            if nums[mid] <= nums[-1]: #go left
                right = mid - 1
            else: # [2,3,1] go right
                left = mid + 1
                
        return nums[left]
    

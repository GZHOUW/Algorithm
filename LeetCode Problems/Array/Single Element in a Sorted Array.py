'''
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
 
Note: Your solution should run in O(log n) time and O(1) space.
'''

def singleNonDuplicate(nums):
    '''
    Demo: [6,6,7,7,8,8,9,10,10]
    left=0(6), right=8(10)
    mid=4(8) --> left=6(9) 
    mid=7(10) --> right=7(10)
    mid=6(9) --> right=6(9)
    loop ends
    '''
    left = 0
    right = len(nums) - 1

    while left < right: # cant use <= because of 'right=mid'
        mid = (right - left)//2 + left

        if mid % 2 == 0: # even
            if nums[mid] == nums[mid+1]: # mid is left of a pair
                left = mid + 2  # target is to the right
            else: # (mid is right of a pair) or single number
                right = mid  # (target is to the left) or is current
        else: # odd
            if nums[mid] == nums[mid+1]:
                right = mid
            else:
                left = mid + 1

    # now, left=right, return either is ok
    return nums[right]

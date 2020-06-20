'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

def moveZeroes(nums):
  """
  Do not return anything, modify nums in-place instead.
  in place, cannot use pop()
  """
  next_zero = 0  # the first zero after a non-zero, to be swapped
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[i], nums[next_zero] = nums[next_zero], nums[i]
      next_zero += 1

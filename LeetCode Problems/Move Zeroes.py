'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
  Input: [0,1,0,3,12]
  Output: [1,3,12,0,0]

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # in place cannot use pop()
    nonzeroPos = 0  # the next position for a non-zero element
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[nonzeroPos] = nums[nonzeroPos], nums[i] # move the cur element to the next non-zero position
            nonzeroPos += 1

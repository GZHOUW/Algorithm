'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white and blue. Use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
come up with a one-pass algorithm using only constant space

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

'''

def sortColors(nums) :
    """
    Demo:
    [2,0,2,1,1,0] front=0, pointer=0, end=5
    [0,0,2,1,1,2] front=0, pointer=0, end=4
    [0,0,2,1,1,2] front=1, pointer=1, end=4
    [0,0,2,1,1,2] front=2, pointer=2, end=4
    [0,0,1,1,2,2] front=2, pointer=2, end=3
    [0,0,1,1,2,2] front=3, pointer=3, end=3
    """

    front = 0
    pointer = 0
    end = len(nums) - 1

    while pointer <= end:
        if nums[pointer] == 0: # move to front
            nums[front], nums[pointer] = nums[pointer], nums[front]
            front += 1
            pointer += 1
        elif nums[pointer] == 2: # move to end
            nums[end], nums[pointer] = nums[pointer], nums[end]
            end -= 1
        else: # find 1, dont move, wait for 0 to swap with 1
            pointer += 1

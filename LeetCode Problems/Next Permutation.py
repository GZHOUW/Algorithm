"""
Do not return anything, modify nums in-place instead.
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

def nextPermutation(nums):
    """
    Demo: [6,4,1,5,3,2]

    firstSmall = 2 (1)
    firstLarge = 5 (2)
    swap(fSmall, fLarge) --> [6,4,2,5,3,1]
    reverse all numbers after firstSmall --> [6,4,2,1,3,5]
    """

    firstSmall = -1 # the first element from the back that is smaller than its next element
    for i in range(len(nums) - 2, -1, -1):# start at the second to last, end at 0 (inclusive)
        if nums[i] < nums[i+1]:
            firstSmall = i
            break

    if firstSmall == -1: # cannot find first small, nums is in decending order
        nums = nums.reverse()  # make it ascending order
        return

    else:
        firstLarge = -1 # the smallest number that [is larger than and on the right of firstSmall]
        for i in range(len(nums) - 1, -1, -1):

            if nums[i] > nums[firstSmall]:
                firstLarge = i
                break

        # swap firstSmall and firstLarge, so firstSmall idx has the next large number
        nums[firstSmall], nums[firstLarge] = nums[firstLarge], nums[firstSmall]

        # reverse all numbers after firstSmall, so they are in ascending order
        nums[firstSmall+1:] = nums[-1: firstSmall: -1]
        return


'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
'''


def searchInsert( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    l = 0
    r = len(nums) - 1

    while l + 1< r: # loop runs when there are at least 3 elements
        mid = (r - l) // 2 + l

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            l = mid + 1

        else:
            r = mid - 1

    # If len < 3 or target not in list
    if target <= nums[l]: # left
        return l
    elif target <= nums[r]:
        return r # mid
    else:
        return r + 1 # right

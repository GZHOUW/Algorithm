'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

def search(nums, target):
    length = len(nums)
    if length == 0:
        return -1

    l = 0
    r = length - 1

    while l < r:
        mid = (r - l)//2 + l # middle position between l and r
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[l]: # mid is in left portion (if = , then mid is the leftmost)
            if nums[mid] >= target and target >= nums[l]: # target is between mid and l
                r = mid -1 # go left
            else:
                l = mid + 1 # go right
        else: # mid is in right portion
            if nums[mid] <= target and target <= nums[r]: # target between mid and r
                l = mid + 1
            else:
                r = mid - 1

    # the loop might not find target, need to check l and r
    if nums[l] == target:
        return l
    elif nums[r] == target:
        return r
    else:
        return -1

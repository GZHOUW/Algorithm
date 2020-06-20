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

def searchRange(nums, target):
      length = len(nums)
      if length == 0:
          return [-1, -1]        
      first = findFirst(nums, target)
      last = findLast(nums, target)
      return [first, last]


def findFirst(nums, target):
    l = 0
    r = len(nums) - 1
    while l  < r:
        mid = (r - l)//2 + l
        if nums[mid] == target:
            if nums[mid - 1] != target or mid == 0: # the first occurence
                return mid
            else:
                r = mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    if nums[l] == target:
        return l
    elif nums[r] == target:
        return r
    else:
        return -1


def findLast(nums, target):
    l = 0
    r = len(nums) - 1
    while l  < r:
        mid = (r - l)//2 + l
        if nums[mid] == target:
            if nums[mid + 1] != target or mid == len(nums)-1: # the last occurence
                return mid
            else:
                l = mid + 1
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    if nums[l] == target:
        return l
    elif nums[r] == target:
        return r
    else:
        return -1

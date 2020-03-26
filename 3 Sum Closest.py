"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

type nums: List[int]
type target: int
rtype: int
"""

def threeSumClosest(self, nums, target):

    nums.sort()
    length = len(nums)

    diff = abs(target - (nums[0] + nums[1] + nums[2]))
    s_res = nums[0] + nums[1] + nums[2]

    for a in range(length):
        b = a + 1
        c = length - 1
        while b < c:
            s = nums[a] + nums[b] + nums[c]
            diff_i = abs(target - s)
            if diff_i < diff:
                diff = diff_i
                s_res = s   
            if s == target:
                return s
            elif s < target:
                b += 1
            else:
                c -= 1
    return s_res

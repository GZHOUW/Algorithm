'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

def fourSum(nums, target):
    sol = []
    length = len(nums)
    if length < 4:
        return sol
    nums.sort()
    for a in range(length - 3):  # (last) three items cannot form a set of four
        if a > 0 and nums[a] == nums[a - 1]:  # nums[a-1] already tested
            continue
        for b in range(a + 1, length - 2): # start after a
            if b > a + 1 and nums[b] == nums[b - 1]:  # nums[b-1] already tested
                continue
            c = b + 1  # left (low) index
            d = length - 1  # right (high) index
            while c < d:
                s = nums[a] + nums[b] + nums[c] + nums[d]
                if s == target:
                    sol.append([nums[a], nums[b], nums[c], nums[d]])  # sorted small - large
                    while c < d and nums[c] == nums[c + 1]:  # no need to test c+1 if they are same
                        # c < d is for index error, ex: [0,0,0]
                        c += 1
                    while c < d and nums[d] == nums[d - 1]:
                        d -= 1
                    c += 1
                    d -= 1
                elif s < target:  # need to be larger
                    c += 1
                else:
                    d -= 1
    return sol

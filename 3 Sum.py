'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
type nums: List[int]
rtype: List[List[int]]

'''
def threeSum(self, nums):

    sol = []
    length = len(nums)
    nums.sort()
    for a in range(length-2): # last two items cannot form a set of three
        if a > 0 and nums[a] == nums[a-1]: # nums[a-1] is the previous target, already tested
            continue
        target = - nums[a] # - a = b + c
        b = a + 1 # idx after target
        c = length - 1 # last idx
        while b < c:
            if nums[b] + nums[c] == target:
                sol.append([nums[a], nums[b], nums[c]]) # sorted small - large
                while b < c and nums[b] == nums[b + 1]: # no need to test b+1 if they are same
                    # b < c is for index error, ex: [0,0,0]
                    b += 1
                while b < c and nums[c] == nums[c - 1]:
                    c -= 1
                b += 1
                c -= 1
            elif nums[b] + nums[c] < target: # need to be larger
                b += 1
            else:
                c -= 1
    return sol

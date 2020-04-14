'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
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
        if a > 0 and nums[a] == nums[a-1]: 
            # If the smallest number is positive, there is no solution
            # nums[a-1] is the previous target, already tested
            continue
        target = - nums[a] # -a = b + c
        b = a + 1 # idx after target
        c = length - 1 # last idx
        while b < c: # perform linear search with two pointers
            if nums[b] + nums[c] == target: # soultion set found
                sol.append([nums[a], nums[b], nums[c]])
                while b < c and nums[b] == nums[b + 1]: # no need to test b+1 if b and b+1 are same
                    # b < c is for index error, ex: [0,0,0]
                    b += 1 # move pointers to neglect duplicates
                while b < c and nums[c] == nums[c - 1]:
                    c -= 1 # move pointers to neglect duplicates
                b += 1 # move pointers
                c -= 1
            elif nums[b] + nums[c] < target: # need to be larger
                b += 1
            else: # need to be smaller
                c -= 1
    return sol

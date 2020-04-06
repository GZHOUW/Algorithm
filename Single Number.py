'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

def singleNumber(nums):
    single = 0
    for i in range(len(nums)):
        single ^= nums[i]
    return single

# 1. a⊕0=a
# 2. a⊕a=0
# therefore, a⊕b⊕a=(a⊕a)⊕b=0⊕b=b

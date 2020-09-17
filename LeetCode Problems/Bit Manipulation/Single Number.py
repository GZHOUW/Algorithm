'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
    Input: [2,2,1]
    Output: 1
    
Example 2:
    Input: [4,1,2,1,2]
    Output: 4
'''

def singleNumber(nums):
    '''
    ^ Bitwise Exclusive XOR:
    Convert two integers to binary form,
    then compare them bit by bit.
    If two bits are the same, XOR outputs 0. 
    If the bits are different, XOR outputs 1.
    '''
    totalXOR = 0
    for num in nums:
        # 0^1^2^3^1^2^3^4 = 0^1^1^2^2^3^3^4 = 0^4 = 4
        totalXOR = totalXOR ^ num
    return totalXOR

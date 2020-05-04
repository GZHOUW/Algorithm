'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
'''

def findComplement(num):
    '''
    Basic Idea: generate a binary number that has the same number of bits as num and every bit is 1,
    then use this number to exclusive or (^) with num
    '''
    i = 1
    while i <= num:
        i = i << 1  # i will be power of 2, e.g. 2(10), 4(100), 8(1000), 16(10000), ect
    return (i-1) ^ num  # i-1 will be 1(1), 3(11), 7(111), 15 (1111), ect
    # ^ : exclusive or ----> 13(1101) ^ 15(1111) = 0010

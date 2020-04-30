'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
'''

def rangeBitwiseAnd(m, n):
    '''
    Rule 1: if a column contain both 1 and 0, its AND value is 0
    Rule 2: if a column's AND value is 0, the AND values of all columns to its right are 0s

    Demo:
    16 --> 10000
    17 --> 10001
    18 --> 10010
    19 --> 10011
           fffcc  where f is fixed, c is changed
    '''
    count = 0
    while m != n: # remove the last bit until m and n are the same (fixed bits)
        m = m >> 1 # right shift: remove the last bit
        n = n >> 1
        count += 1
    return m << count # left shift: add a 0 at the end, add zeros (changed bits) to the fixed bits

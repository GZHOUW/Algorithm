'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = truncate(-2.33333..) = -2.

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''

class Solution:
    '''
    repeatedly subtract divisor from dividend, until there is none enough left. Then the count of subtractions will be the answer. Yet this takes linear time and is thus slow. A better method is to subtract divisor in a more efficient way. We can subtract divisor, 2divisor, 4divisor, 8*divisor... as is implemented above.
    '''
    def divide(self, dividend, divisor):
        isPositive = (dividend < 0) == (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0 # res
        
        while dividend >= divisor: # if less, return 0
            temp = divisor # the current divisor
            i = 1 # number of divisors that get subtracted
            
            while dividend >= temp:
                dividend -= temp
                quotient += i
                i <<= 1 # *= 2
                temp <<= 1 # *= 2
        if not isPositive:
            quotient = -quotient
        return min(max(-2147483648, quotient), 2147483647)

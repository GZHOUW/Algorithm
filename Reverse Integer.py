'''
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

type x: int
rtype: int

'''

class Solution(object):
    def reverse(self, x):
        """
        :
        """
        if x < 0:
            result = '-'
            x_str = str(-x)
        else:
            result = ''
            x_str = str(x)
        n = len(x_str) - 1
        count_0 = False
        while n >= 0:
            if (not count_0) and x_str[n] != 0:
                result += x_str[n]
                count_0 = True
            elif count_0:
                result += x_str[n]
            n -= 1
        if abs(int(result)) > 2147483648:
            return 0
        return(int(result))
        

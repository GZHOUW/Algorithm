'''
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
def isHappy(n):  
    while n != 1:
        n_i = 0
        for digit in str(n):
            n_i += int(digit) ** 2
        n = n_i
        if n == 4: # False conditions always converge to 4
            return False
    return True
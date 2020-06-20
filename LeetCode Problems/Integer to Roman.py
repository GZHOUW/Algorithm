'''
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: 3
Output: "III"

Example 2:
Input: 4
Output: "IV"

Example 3:
Input: 9
Output: "IX"

Example 4:
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

def intToRoman(num):
    # Corresponding roman str and int, all possibilities
    romanStr = ['M', 'CM', 'D', 'CD', 'C','XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    romanInt = [1000, 900, 500,  400, 100, 90,  50,   40,   10,   9,   5,    4,   1]
    res = ""  
    i = 0 
    while num > 0: # try to add largest number, if cannot add, try smaller numbers
        if num - romanInt[i] >= 0:
            res += romanStr[i]
            num -= romanInt[i]
        else:
            i += 1
    return res

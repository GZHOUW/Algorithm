'''
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4
'''

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL': 40, 'XC':90, 'CD':400, 'CM': 900}
    result = 0
    i = 0
    while i < len(s):
        if i != len(s) - 1:
            if (s[i] + s[i+1]) in roman_dict:
                result += roman_dict[s[i] + s[i+1]]
                i += 2
            else:
                result += roman_dict[s[i]]
                i += 1
        else:
            result += roman_dict[s[i]]
            i += 1
    return result

print(romanToInt('DCXXIV'))

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        l = len(s)
        while l > 0:
            start = 0
            end = l
            while end <= len(s):
                substring = s[start:end]
                if substring == substring[::-1]:
                    return substring
                start += 1
                end += 1
            l -= 1
        

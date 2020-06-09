'''
Given a string s and a string t, check if s is subsequence of t. A subsequence of a string is a new string which is 
formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''

class Solution:
    def isSubsequence(self, s, t):
      
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False 

        s_idx = 0 
        for char in t: # Iterate through each character in t
            if s[s_idx] == char: # Match found
                s_idx += 1 # advance to next s character
                if s_idx == len(s): # reached the end of t
                    return True

        return False

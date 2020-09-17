'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
    Input: "aba"
    Output: True

Example 2:
    Input: "abca"
    Output: True
    
Explanation: You could delete the character 'c'.
'''

class Solution:
    def validPalindrome(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] == s[right]: # ignore already palindrome chars
                left += 1
                right -= 1
            else:
                # try deleting both left and right 
                return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)
        return True
    
    def isPalindrome(self, s, left, right):
        # determines whether s[left:right] is a palindrome
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

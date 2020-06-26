class Solution:
    def isPalindrome(self, s):
        if not s:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            # get rid of non-alphanumeric chars
            while left < right and (not s[left].isalnum()):
                left += 1
            while left < right and (not s[right].isalnum()):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

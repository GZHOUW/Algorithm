'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
    Input:
    s = "aa"
    p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    
Example 2:
    Input:
    s = "aa"
    p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    
Example 3:
    Input:
    s = "ab"
    p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".
    
Example 4:
    Input:
    s = "aab"
    p = "c*a*b"
    Output: true
    Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
    
Example 5:
    Input:
    s = "mississippi"
    p = "mis*is*p*."
    Output: false
'''

class Solution:
    def isMatch(self, s, p):
        # Create 2D dp matrix: dp[i][j] stores bolean value: whether s[0:i] matches with p[0:j]
        # Extra row and col are for s[0:0] and p[0:0] (empty)
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True # p[0:0]='', s[0:0]='' ---> matches -->True
        
        for r in range(2,len(dp)): # iterate through first col (p)
            if p[r-1] == '*' and dp[r-2][0]:
                dp[r][0] = True

        for r in range(1, len(dp)): # dp[1] --> p[0]
            for c in range(1, len(dp[0])): # dp[][1] --> s[0]     
                # current two chars match --> doesnt change previous relationship
                if s[c-1] == p[r-1] or p[r-1] == '.': 
                    dp[r][c] = dp[r-1][c-1] 
                
                elif p[r-1] == '*':
                    
                    # [r-2]: repeat prev p element 0 time (eliminate prev), [r-1]:repeat once (* equals nothing)
                    dp[r][c] = dp[r-2][c] or dp[r-1][c]

                    # If prev p is equal to current s, with helps of *, can be true
                    if p[r-2] == s[c-1] or p[r-2] == '.':
                        dp[r][c] |= dp[r][c - 1]
          
        return dp[-1][-1]

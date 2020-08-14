'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    '''
    Algorithm: Keep a sliding window *substring) when iterating through the array, and keep a dictionary that contains the last occurence of every element
               if the cur char has appeared before, set he left boundary as the char after the last occurence of cur char (start a new substring there to
               avoid duplicate)
               update length along the way
    '''
    def lengthOfLongestSubstring(self, s):
        start = 0
        cur = 0
        idx = dict() # key = char, val = id of the char's last occurence
        maxLen = 0
        curLen = 0
        
        while cur < len(s):
            #    duplicate   &  the previous occurence is after start (within the current substring)
            if s[cur] in idx and idx[s[cur]]>= start:
                maxLen = max(maxLen, curLen)
                start  = idx[s[cur]]+1
                
            idx[s[cur]] = cur # {'a':1}
            
            curLen = cur-start + 1
            print(curLen)
            cur += 1
        maxLen = max(maxLen, curLen)
        return maxLen

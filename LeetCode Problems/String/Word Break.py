'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
             
Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution:
   
    def wordBreak(self, s, wordDict): # Time: O(n^2), Space: O(n)
        '''
        Algorithm:
        1. create a memo array where memo[i] is bolean--> is s[i:] valid (can be segmented)
        2. call isValid to check if s[0:] is valid
        '''
        memo = [None for _ in s]
        return self.isValid(s, wordDict, 0, memo)
        
        
    def isValid(self, s, d, start, memo):
        '''
        Algorithm:
        1. if the current substring s[start:] is empty, we reached the end --> return True
        2. if current substring was checked before, return the result directly from memo
        3. for i from 'start' to end of s
            3.1. curword is s[start:i]
            3.2. if curword in dict and s[i+1:] is valid ---> all s is valid--> return True
        4. If program didnt return True until the end, return False
        '''
        if start == len(s):
            return True
        
        if memo[start] != None: # already know if s[start:] is valid
            return memo[start]
        
        for i in range(start, len(s)):
            curWord = s[start:i+1]
            if curWord in d and self.isValid(s, d, i+1, memo):
                memo[start] = True
                return True
            
        memo[start] = False
        return False


        

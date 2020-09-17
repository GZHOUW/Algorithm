'''
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
You may assume both s and t have the same length.

Example 1:
    Input: s = "egg", t = "add"
    Output: true

Example 2:
    Input: s = "foo", t = "bar"
    Output: false

Example 3:
    Input: s = "paper", t = "title"
    Output: true


'''

class Solution:
    '''
    Algorithm: 
        keep two dicts d1 and d2
        key = char, val = a list of index where char occur in string
        if the vals of d1 and d2 are same, return true
    
    '''
    def isIsomorphic(self, s, t):
        d1, d2 = {}, {}
        for i, char in enumerate(s): # 'add' --> {'a':[0], 'd':[1,2]}
            if char in d1:
                d1[char].append(i)
            else:
                d1[char] = [i]
            
        for i, char in enumerate(t): # 'egg' --> {'e':[0], 'g':[1,2]}
            if char in d2:
                d2[char].append(i)
            else:
                d2[char] = [i]
        # change from 'dictvalue' to list
        return list(d1.values()) == list(d2.values())
        

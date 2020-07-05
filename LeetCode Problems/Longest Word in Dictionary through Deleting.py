'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. 
If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
    Input:
    s = "abpcplea", d = ["ale","apple","monkey","plea"]
    Output: 
    "apple"

Example 2:
    Input:
    s = "abpcplea", d = ["a","b","c"]
    Output: 
    "a"
    
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
'''


class Solution:
    def findLongestWord(self, s, d):
        res = ''
        for word in d: #                   longer result, update    same length but smaller lexicographical order
            if self.isWordInS(s, word) and (len(word) > len(res) or (len(word) == len(res) and word < res)):
                res = word
        return res
            
    def isWordInS(self, s, word):
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(word) # word pointer reached end, meaning entire word can be found in s

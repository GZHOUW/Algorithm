'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    # count freq method: time complexity O(n)
    def groupAnagrams(self, strs):
        anagrams = dict() # key = a base anagram, value: a list containing all the anagram of the base case
        for string in strs:
            # create a dict of freq of string's chars
            freq = [0] * 26
            for char in string:
                freq[ord(char)-ord('a')] += 1
            freqStr = ''
            for i in range(len(freq)):
                if freq[i] != 0:
                    freqStr += chr(i + ord('a'))
                    freqStr += str(freq[i])
            if freqStr not in anagrams:
                anagrams[freqStr] = [string]
            else:
                anagrams[freqStr].append(string)
        res = []
        for key in anagrams:
            res.append(anagrams[key])
        return res
    
    ''' Sorting solution --> time complexity = O(n*logn)
    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return []
        res = []
        anagram = dict()
        
        for i in range(len(strs)):
            str_list = list(strs[i]) # ['e','a','t']
            str_list.sort() # ['e','a','t'] ---> ['a','e','t']
            str_sorted = ''.join(str_list) # ['a','e','t'] --> 'aet'
            if str_sorted in anagram:
                anagram[str_sorted].append(strs[i]) # {['a','e','t']: ['eat','ate']}
            else:
                anagram[str_sorted] = [strs[i]] # create new key
        res = list(anagram.values())
        return res
            
    '''

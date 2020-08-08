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
    '''
    Algorithm:  1. Create a dict where key is a base string and value is a list containing all the anagrams of the base string
                2. For every string in strings, do the following:
                    2.1. Create a len=26 frequency list that contains how many times each char appear. E.g. "addf"-->[1,0,0,2,0,1,...]
                    2.2. Convert frequency list to a frequency string. E.g. [1,0,0,2,0,1,...]--> "1a2d1f"
                    2.3. Let frequency string be the key of dict and the string itself as the val
                3. Transform the dict into list and return
    
    '''
    def groupAnagrams(self, strs): # count freq method: time complexity O(n)
        anagrams = dict() # key = a base string, value: a list containing all the anagram of the base string
        for string in strs:
            # create a dict of freq of string's chars
            freq = [0] * 26
            for char in string:
                freq[ord(char)-ord('a')] += 1
            freqStr = ''
            for i in range(len(freq)):
                if freq[i] != 0:
                    freqStr += str(freq[i])
                    freqStr += chr(i + ord('a'))
                    
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

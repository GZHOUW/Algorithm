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

def groupAnagrams(strs):
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

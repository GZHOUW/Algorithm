'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
  Input:
  "tree"
  Output:
  "eert"
  Explanation:
  'e' appears twice while 'r' and 't' both appear once.
  So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
  
Example 2:
  Input:
  "cccaaa"
  Output:
  "cccaaa"
  Explanation:
  Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
  Note that "cacaca" is incorrect, as the same characters must be together.
'''

class Solution:
    def frequencySort(self, s):
        freqDict = dict()
        res = ""
        for char in s:
            if char not in freqDict:
                freqDict[char] = 1
            else:
                freqDict[char] += 1
        
        bucket = ['' for _ in range(len(s)+1)]
        
        for char, freq in freqDict.items():
            bucket[freq] += char * freq
        
        res = ''
        
        for row in reversed(bucket):
            res += row

        return res

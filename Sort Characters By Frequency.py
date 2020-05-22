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

def frequencySort(self, s: str) -> str:
    freq = dict()
    res = ""
    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    s_list = sorted(freq, key=lambda x: freq[x], reverse = True)

    for char in s_list:
        res += char * freq[char]

    return res

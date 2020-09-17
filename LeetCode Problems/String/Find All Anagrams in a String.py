'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

from collections import Counter
def findAnagrams(s, p):
    sLen = len(s)
    pLen = len(p)
    if sLen < pLen:
        return []

    sFreq = Counter()
    pFreq = Counter(p)
    res = []

    for i in range(sLen):
        sFreq[s[i]] += 1
        if i >= pLen:  # dont start until a full window has been created
            if sFreq[s[i - pLen]] == 1:  # decrement the first char of anagram
                del sFreq[s[i - pLen]]
            else:
                sFreq[s[i - pLen]] -= 1
        if pFreq == sFreq:
            res.append(i - pLen + 1)

    return res

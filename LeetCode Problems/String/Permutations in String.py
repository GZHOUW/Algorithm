'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
'''


class Solution:
    def checkInclusion(self, s1, s2):
        '''
        Algorithm: check if s2[i-len(s1):i] is a permutation of s1
            1. create a counter for s1 (s1 freq) and an emoty counter for s2
            2. iterate through s2, delete the elements before i-len(s1)
            3. check if freq1 and freq2 are equal
        '''
        s1Len = len(s1)
        s2Len = len(s2)
        if s1Len > s2Len:
            return False

        s1Freq = Counter(s1)
        s2Freq = Counter()
        for i in range(s2Len):
            s2Freq[s2[i]] += 1

            if i >= s1Len:
                if s2Freq[s2[i - s1Len]] == 1:
                    del s2Freq[s2[i - s1Len]]
                else:
                    s2Freq[s2[i - s1Len]] -= 1

            if s1Freq == s2Freq:
                return True

        return False
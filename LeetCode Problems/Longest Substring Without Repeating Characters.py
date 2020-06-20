'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    length = []
    for i in range(len(s)):
        substring = ''
        idx = 0
        while (i + idx < len(s)) and (s[i + idx] not in substring): 
            # second condition is not evaluated if the first is False
            substring += s[i + idx]
            idx += 1
        length.append(len(substring))
    if length == []:
        return 0
    return max(length)

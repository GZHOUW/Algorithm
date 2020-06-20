'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

def firstUniqChar(s):
    occur = dict()  # {char: occurence}
    for i in range(len(s)):  # create dictionary
        if s[i] in occur:
            occur[s[i]] += 1
        else:
            occur[s[i]] = 1

    for i in range(len(s)):
        if occur[s[i]] == 1:  # return first unique
            return i
    return -1

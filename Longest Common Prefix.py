'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

def longestCommonPrefix(strs):
    if not strs:
        return ""
    pre = strs[0]

    for i in range(1, len(strs)):
        new_pre = ''
        for j in range(min(len(strs[i]), len(pre))):
            if strs[i][j] == pre[j]: 
                new_pre += strs[i][j] # find common prefix
            else:
                break

        if new_pre == '':
            return ''
        pre = new_pre

    return pre

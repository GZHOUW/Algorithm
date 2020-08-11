'''
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that 
each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
'''

class Solution:
    def partitionLabels(self, S): # Time: O(n), Space: O(1)
        '''
        Algorithm: 
        1. Create a dict with key=char, cal=[idx of 1st appear, idx of last appear]
        2. Merge the overlapping intervals and put all into a list
        3. Return the length of each interval in the list intervals
        '''
        
        dic = {} # At most 26 keys
        for i, char in enumerate(S):
            if char in dic:
                dic[char][1] = i
            else:
                dic[char] = [i, i]
        
        intervals = []
        for key in dic:
            if intervals == [] or dic[key][0] > intervals[-1][1]: # new interval
                intervals.append(dic[key])
            elif dic[key][0] < intervals[-1][1] < dic[key][1]: # update interval[1]
                intervals[-1][1] = dic[key][1]
        
        # return the length of each merged interval
        return [interval[1]-interval[0]+1 for interval in intervals]
    
    def optimized(self, S):
        dic = {} # stores the idx of last appearance of each char
        for i, char in enumerate(S):
            dic[char] = i
        
        res = []
        start = 0 # start and end of cur interval
        end = 0
        for i, char in enumerate(S):
            end = max(end, last[char])
            if i == end:
                res.append(end - start + 1)
                start = i + 1 # move on to new interval
        return res

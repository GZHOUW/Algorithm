'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
    Input: [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
    Input: [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
    Input: [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        
        intervals = sorted(intervals, key=lambda x: x[1]) # sort intervals by acsending upper bound
        count = 1 # the max number of intervals that DONT overlap
        end = intervals[0][1]
        
        for interval in intervals:
            if interval[0] >= end:  # NO overlap
                end = interval[1]
                count += 1
        return len(intervals) - count # subtract max no-overlap to get min-overlap

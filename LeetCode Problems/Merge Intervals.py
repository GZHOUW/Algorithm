'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

def merge(intervals):
    if len(intervals) == 0:
        return None
    intervals.sort()
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]: # left bound < merged right bound
            if intervals[i][1] > merged[-1][1]: # right bound < merged right bound
                merged[-1][1] = intervals[i][1]  # update merged right bound 
        else:
            merged.append(intervals[i]) # new merged interval
    return merged

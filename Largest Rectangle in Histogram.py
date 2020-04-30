'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Example:
Input: [2,1,5,6,2,3]
Output: 10
'''

def largestRectangleArea(heights):
    '''
    demo:
    heights = [5,5,1,7,2,7,6]
    left =    [1,2,3,1,2,1,2]
    right =   [2,1,5,1,3,1,1]
    '''

    n = len(heights)
    left = [1]*n # number of continuous bars to the left (including bar[i]) that have values greater or equal than the value of bar[i] 
    right = [1]*n # number of continuous bars to the right (including bar[i]) that have values greater or equal than the value of bar[i] 

    for i in range(1,n): # start from second because first must be 1
        j = i - 1
        while j >= 0 and heights[j] >= heights[i]:
            j -= left[j] # search to the left
        left[i] = i - j

    for i in range(n-2, -1, -1):
        j = i + 1
        while j < len(heights) and heights[i] <= heights[j]:
            j += right[j]  # search to the right
        right[i] = j - i

    area = 0
    for i in range(n):
        area = max(area, heights[i]*(left[i] + right[i] - 1))
        '''
        heights[i]: the value of current bar:
        left[i] + right[i] - 1: the bars to the left and right of bar[i] that have greater (or equal) values than bar[i]
        '''
    return area


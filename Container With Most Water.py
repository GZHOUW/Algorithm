'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    area_max = 0
    l = 0
    r = len(height) - 1

    while (l < r): # loop ends when r_idx - l_idx = 1
        area_i = min(height[l], height[r]) * (r - l) # shorter height * length of base
        area_max = max(area_max, area_i) # update max area
        if height[l] > height[r]: # move the shorter line so that area can may get larger
            r -= 1
        else:
            l += 1
    return area_max


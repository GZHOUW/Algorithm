'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:
    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
'''
def trap(height):
    left = 0
    right = len(height) - 1
    water = 0
    lMax = 0
    rMax = 0

    while left < right:
        if height[left] < height[right]: # left (shorter) determines amount of water
            lMax = max(lMax, height[left])
            water += (lMax - height[left]) * 1 # the amount of water that can be contained by cur bar
            # if lMax is cur, water += 0
            # if lMax is on the left of cur, means water can be contained
            left += 1
        else:
            rMax = max(rMax, height[right])
            water += rMax - height[right]
            right -= 1
    return water

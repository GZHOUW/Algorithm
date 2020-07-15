'''
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
Example 1:
    Input: hour = 12, minutes = 30
    Output: 165
    
Example 2:
    Input: hour = 3, minutes = 30
    Output: 75
'''

class Solution:
    def angleClock(self, hour, minutes):
        if hour==12:
            h = (minutes/60)*30
        else:
            h = (hour/12)*360 + (minutes/60)*30
        m = (minutes/60)*360
        if m > h:
            return min(m-h, 360-(m-h))
        else:
            return min(h-m, 360-(h-m))
            

'''
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:
    "G": go straight 1 unit;
    "L": turn 90 degrees to the left;
    "R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:
    Input: "GGLLGG"
    Output: true
    Explanation: 
    The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
    When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
    
Example 2:
    Input: "GG"
    Output: false
    Explanation: 
    The robot moves north indefinitely.
    
Example 3:
    Input: "GL"
    Output: true
    Explanation: 
    The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
'''

class Solution:
    def isRobotBounded(self, instructions):
        '''
        Algorithm: 1. Find the location of the robot after one cycle, if at origin, TRUE
                   2. Find the facing direction of the robot after one cycle, if north, FALSE
                      a. 其实我们不需要考虑中间步骤， 只需要考虑最后的位置[x,y], 那么就是方向朝北的情况下， 
                         会从[0,0]到[x,y]有一个线段，无论中间过程是怎么样，结果就是从[0,0]–>[x,y]
                      b. 如果方向继续朝北， 那么后面就是[2x,2y], [3x,3y]….
                   3. If face other directions, TRUE
        '''
        x = 0
        y = 0
        d = 0 # north
        for char in instructions:
            if char == 'G':
                if d % 4 == 0:
                    y += 1
                elif d % 4 == 1:
                    x += 1
                elif d % 4 == 2:
                    y -= 1
                elif d % 4 == 3:
                    x -= 1
            elif char == 'L':
                d -= 1
            elif char == 'R':
                d += 1
        
        if x == y == 0: # back at origin
            return True
        elif d % 4 == 0:
            return False
        return True

'''
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:
sx, sy, tx, ty will all be integers in the range [1, 10^9].
'''

class Solution:
    def reachingPoints(self, x1, y1, x2, y2):
        '''
        Reachable points can be represented as a binary tree, where root is (x1,y1)
                   (x,y)
                  /    \
            (x+y,y)     (x, x+y)
           /       \          
  (x+y+y,y)         (x+y,x+y+y)
  
        Algorithm: 
        1. Start from the bottom node(x2,y2), there is only one way from bottom node to root
        2. Go upwards by doing (x2,y2) --> (x2-y2-y2-y2..., y2) -->(x2%y2, y2)
           --> up the tree along a straight path
        '''
        
        if x2 < x1 or y2 < y1:
            return False
        if x1 == x2: # x can be reached, need to check y
            #return y2 % x1 == y1 # subtract x1 every layer, see if y2 remains
            return (y2-y1) % x1 == 0
        if y1 == y2:
            #return x2 % y1 == x1
            return (x2-x1)%y1==0
        
        if x2 > y2:  # (x+y,y)
            x2 %= y2
        else: # (x,x+y)
            y2 %= x2
        return self.reachingPoints(x1, y1, x2, y2)

'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	 -3	   3
-5	    -10	   1
10	     30	  -5 (P)
'''

class Solution:
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return None
        
        health = [[0 for _ in dungeon[0]] for __ in dungeon] 
        # health[r][c] contains the the minimum required health of the prince when he enters dungeon[r][c] so that he is able to rescue the princess
        # the least hp knight must have at each cell so that 1 hp remains after last cell

        
        for r in range(len(dungeon)-1, -1, -1): # start from bottom right with 1 hp, the minimum win condition
            for c in range(len(dungeon[0])-1, -1, -1):
                cur = dungeon[r][c]
                if r == len(dungeon)-1 and c == len(dungeon[0])-1: # bottom right
                    health[r][c] = max(1, 1 - cur)  
                    # if last cell has monster, must have 1-dungeon[r][c] health when entering
                    
                elif r == len(dungeon)-1: # last row
                    health[r][c] = max(1, health[r][c+1] - cur)
                    # if cur cell has a big potion, health[r][c+1]-cur will be negative, so 1 health is enough
                    
                elif c == len(dungeon[0])-1: # last col
                    health[r][c] = max(1, health[r+1][c] - cur)
                else:
                    health[r][c] = max(1, min(health[r][c+1], health[r+1][c]) - cur)
                    # min(health[r][c+1], health[r+1][c]) finds the optimum path, use as little health as possible so that health[0][0]will have the minimum initial health
                                                    
        
        return health[0][0]

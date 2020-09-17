'''
Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

Example 1:
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]

Example 2:
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 
Constraints:
|x| + |y| <= 300
'''

class Solution:
    def minKnightMoves(self, x, y):
        '''
        Algorithm: Breath First Search: good for finding shortest paths on unweighted graphs
        check the 8 neighbors first (2,1),(1,2)...(-1,2), and then check 8 neighbors for each of them, ... until the res is found
        
        '''
        # If we are already at the destination, no moved needed
        if x == 0 and y == 0:
            return 0
        
        frontier = collections.deque()
        
        # Add source node into queue
        frontier.append((0, 0, 0)) # x,y,the minimum number of steps needed to get to (x,y)
        
        # Set for keeping track of nodes we have visited so far
        visited = set()
        #all possible movments for the knight 
        x_moves = [2, 2, -2, -2, 1, 1, -1, -1] 
        y_moves = [1, -1, 1, -1, 2, -2, 2, -2]
        
        visited.add((0, 0)) # keeps nodes that are already checked
        while frontier:
            
            i, j, steps = frontier.popleft() # pop the earliest added node
            # Check if we have reached the destination
            if i == x and j == y:
                return steps
            
            for dx, dy in zip(x_moves, y_moves):
                newi, newj = i + dx, j + dy
                
                if (newi, newj) not in visited:
                    visited.add((newi, newj))
                    frontier.append((newi, newj, steps+1))

'''
You have some sticks with positive integer lengths.
You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  
You perform this action until there is one stick remaining.
Return the minimum cost of connecting all the given sticks into one stick in this way.

Example 1:
  Input: sticks = [2,4,3]
  Output: 14

Example 2:
  Input: sticks = [1,8,3,5]
  Output: 30

Constraints:

1 <= sticks.length <= 10^4
1 <= sticks[i] <= 10^4
'''

class Solution:
    def connectSticks(self, sticks):
        heapq.heapify(sticks) # min heap: a tree where each node is smaller than its children, root node is min
        res = 0
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks) # always connect two shortest sticks
            res += x + y
            heapq.heappush(sticks, x + y) # add new stick to heap
        return res

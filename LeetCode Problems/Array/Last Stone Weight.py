'''
We have an array of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y. 

The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
'''

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        self.lastWeight = 0
        self.smash(stones)
        return self.lastWeight
    
    def smash(self, stones): # void function, returns nothing
        if len(stones) == 0:
            self.lastWeight = 0 # modify lastWeight
        elif len(stones) == 1:
            self.lastWeight = stones[0] # modify lastWeight
        else:
            stones.sort() # access largest two stones
            stone1 = stones.pop()
            stone2 = stones.pop()
            stones.append(stone1 - stone2) # smash, get remaining weight
            self.smash(stones) # recurse

'''
Given an array w of positive integers, where w[i] describes the weight of index i, 
write a function pickIndex which randomly picks an index in proportion to its weight.
In the case w = [1, 99] , your pickIndex() should return 1 for 99% and 0 for 1%.
'''

class Solution:

    def __init__(self, w: List[int]):
        self.weight = w
        self.length = len(w)
        
        # construct weight into a prefix sum array: ex:[2,3,5,1]-->[2,5,10,11]
        for i in range(1, self.length):
            self.weight[i] += self.weight[i-1]
            
    def pickIndex(self) -> int:
        rand = random.random() * self.weight[-1]  # random() returns a rand value between 0 and 1, multiply by last element of weight, which is the range
        left = 0
        right = self.length - 1
        # perform binary search to see rand is between which two index
        while left <= right:
            mid = (right - left)//2 + left
            if self.weight[mid-1] < rand < self.weight[mid]:
                return mid
            elif self.weight[mid] < rand: # go right
                left = mid + 1
            else:
                right = mid - 1
        return left
                

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

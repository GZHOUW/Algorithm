'''
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.
(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
Return the number of good subarrays of A.

Example 1:
    Input: A = [1,2,1,2,3], K = 2
    Output: 7
    Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

Example 2:
    Input: A = [1,2,1,3,4], K = 3
    Output: 3
    Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Note:
    1 <= A.length <= 20000
    1 <= A[i] <= A.length
    1 <= K <= A.length
'''

class Solution:
    def subarraysWithKDistinct(self, A, K):
        # (At most 4 NDI) - (At most 3 NDI) = 4 NDI
        return  self.subarraysWithAtMostKDistinct(A,K) - self.subarraysWithAtMostKDistinct(A, K-1)
    
    
    def subarraysWithAtMostKDistinct(self, A, K):
        start = cur = 0
        subarray = collections.defaultdict(int) # the frequency of ints in cur subarray
        NDI = 0 # Number of Distinct Integers
        res = 0
        
        while cur < len(A):
            # if the cur int is new to the current subarray, add 1 to NDI
            if subarray[A[cur]] == 0:
                NDI += 1
                
            subarray[A[cur]] += 1 # add frequency
            
            # While NDI is too big so that current subarray is invalid
            while NDI > K:
                if subarray[A[start]] == 1: # when freq change from 1 to 0, NDI-1
                    NDI -= 1
                    
                # move start one step to the right, meaning its occurence -1
                subarray[A[start]] -= 1 
                start += 1
                
            if NDI <= K: # Now start and NDI are correct, update res
                res += cur - start + 1 
            cur += 1
        return res

'''
Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:

Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.
 

Example 1:

Input: nums1 = [7,4], nums2 = [5,2,8,9]
Output: 1
Explanation: Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8). 
Example 2:

Input: nums1 = [1,1], nums2 = [1,1,1]
Output: 9
Explanation: All Triplets are valid, because 1^2 = 1 * 1.
Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]^2 = nums2[j] * nums2[k].
Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].
Example 3:

Input: nums1 = [7,7,8,3], nums2 = [1,2,9,7]
Output: 2
Explanation: There are 2 valid triplets.
Type 1: (3,0,2).  nums1[3]^2 = nums2[0] * nums2[2].
Type 2: (3,0,1).  nums2[3]^2 = nums1[0] * nums1[1].
Example 4:

Input: nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
Output: 0
Explanation: There are no valid triplets.
'''

class Solution:
    # O(N*M) Solution
    def numTriplets(self, nums1, nums2): 
        res = 0
        for n in nums1:
            res += self.twoProduct(n*n, nums2)
        for n in nums2:
            res += self.twoProduct(n*n, nums1)
        
        return res
    
    
    def twoProduct(self, target, nums):
        count = 0
        compFreq = {} # key: compliment (target/cur), element: freq of this compliment (NOT idx!!!)
        for i in range(len(nums)):
            comp = target / nums[i]
            if comp == int(comp): # is comp is a float, no need to proceed
                if nums[i] in compFreq:
                    count += compFreq[nums[i]]
                
                if comp in compFreq: # update freq
                    compFreq[comp] += 1
                else:
                    compFreq[comp] = 1
        return count
                
                
    '''
    # O(N^2) Solution
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int: 
        res = 0
        
        # freq is dict that has key=n^2, element=frequency of n^2 occur
        # if there are duplicate in nums1=[2,2], and nums2=[1,4], there are 2 cases in stead on 1
        freq1 = {}
        freq2 = {}
        for n in nums1:
            if n*n in freq1:
                freq1[n*n] += 1
            else:
                freq1[n*n] = 1
        for n in nums2:
            if n*n in freq2:
                freq2[n*n] += 1
            else:
                freq2[n*n] = 1
        
        for b in range(len(nums2)-1):
            for c in range(b+1, len(nums2)):
                if (nums2[b] * nums2[c]) in freq1:
                    res += freq1[nums2[b] * nums2[c]]
                    
        for b in range(len(nums1)-1):
            for c in range(b+1, len(nums1)):
                if (nums1[b] * nums1[c]) in freq2:
                    res += freq2[nums1[b] * nums1[c]]
        return res
    '''

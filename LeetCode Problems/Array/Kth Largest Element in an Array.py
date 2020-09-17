'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
    Input: [3,2,1,5,6,4] and k = 2
    Output: 5

Example 2:
    Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4
    
Note:
    You may assume k is always valid, 1 ≤ k ≤ array's length.
'''


class Solution:
    def findKthLargest(self, nums, k):
        numsSorted = self.mergeSort(nums)
        return numsSorted[k-1]
    
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        else:
            a = nums[:len(nums)//2]
            b = nums[len(nums)//2:]
            aSorted = self.mergeSort(a) # always start with single digit number
            bSorted = self.mergeSort(b)
            c = []
            i = 0
            j = 0
            while i < len(aSorted) and j < len(bSorted):
                if aSorted[i] >= bSorted[j]:
                    c.append(aSorted[i])
                    i += 1
                else:
                    c.append(bSorted[j])
                    j += 1
            while i < len(aSorted):
                c.append(aSorted[i])
                i += 1

            while j < len(bSorted):
                c.append(bSorted[j])
                j += 1
            return c

'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
'''

class Solution:
    def topKFrequent(self, nums, k):
        # nums = [1,1,1,2,2,3]
        freqDict = {} # {1:3, 2:2, 3:1}
        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
                
        bucket = [[] for _ in range(len(nums)+1)] 
        '''
        bucket[i] denotes a list of numbers that have a frequency of i
        therefore the rightmost non-empty list comtains the most frequent numbers
        e.g. nums = [1,1,1,2,2,3] ----> [],[3],[2],[1],[],[],[]]
        '''
        for num, freq in freqDict.items():
            bucket[freq].append(num)

        res = []

        for row in reversed(bucket): # get the k most frequent numbers
            if not row:
                continue
            else:
                for i in range(len(row)):
                    res.append(row[i])
                    if len(res) == k:
                        return res

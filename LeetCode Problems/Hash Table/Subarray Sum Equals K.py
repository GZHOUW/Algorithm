'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
'''

def subarraySum(nums, k):

    sDict = {0:1} 
    '''
    nums = [1,2,1,3]
    k = 3
    key = the running sums: [0,1,3,4,7]
        - must include 0
        - [1,2,1,3] and k = 3 ---> [0,1,3,4,7]---> 3-0=k (s-k = 0), 4-1=k (s-k=1), 7-4=k (s-k = 4)
    item: frequencies that the running sum (key) occured
    '''

    s = 0 # running sum
    count = 0 # result
    for i in range(len(nums)):
        s += nums[i]  # s = sum(nums[0:i+1]) sum from 0 to i

        if s - k in sDict:
            count += sDict[s-k] 
            '''
            if [current s - previous s = k], subarray found
            that is equivilant to [current s - k = previous s]
            += sDict[s-k] instead of += 1 because there might be several same previous s
            '''

        if s in sDict: # already exist in dict, +1 to frequency
            sDict[s] += 1
        else: # create new key, freq = 1
            sDict[s] = 1

    return count


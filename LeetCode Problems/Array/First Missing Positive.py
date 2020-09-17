'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
'''

def firstMissingPositive(nums):
    if not nums: 
        return 1
    nums.append(0) # placeholder for index 0
    length = len(nums)

    # move element with value x to index [x]
    for i in range(length): 
        cur = nums[i]
        while cur >=0 and cur < length and cur != nums[cur]:
            '''
            stop the loop when:
            1. cur is 0 or negative (invalid)
            2. exceeds the last index (too large, don't need to be considered)
            3. cur is already at the correct position (e.g. at index [cur])
            '''
            temp = nums[cur]
            nums[cur] = cur
            cur = temp

    #Pass 2, find first location where the index doesn't match the value
    for i in range(length):
        if nums[i] != i:
            return i
    return length

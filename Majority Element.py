'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''
    def majorityElement(self, nums):
        '''
        the idea here is if a pair of elements from the
        list is not the same, then delete both, the last 
        remaining element is the majority number
        '''
        count = 0
        for num in nums:
            if count == 0: # all previous numbers canceled out, fresh start
                count += 1
                major = num;
            elif major == num: # current is major, add count
                count += 1
            else: 
                count -= 1 # cancel out major and current [1,1,1,2,2,2,...]
        return major

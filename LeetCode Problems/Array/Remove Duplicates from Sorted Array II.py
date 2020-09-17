'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
It doesn't matter what you leave beyond the returned length.

Example 1:
Given nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

Example 2:
Given nums = [0,0,1,1,1,1,2,3,3],
Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

'''

def removeDuplicates(nums):
    # Better Method

    if len(nums) <= 2:
        return 2
    idx = 2
    for num in nums[2:]:
        if num != nums[idx - 2]:
            nums[idx] = num
            idx += 1
    return idx

    ''' #Own Method
    if len(nums) <= 2:
        return 2
    idx = 1
    one = 0
    two = None

    for i in range(1, len(nums)):
        if not two:
            if nums[i] == nums[one]: # found first duplicate
                two = i
                idx += 1
            else:
                one = i
                idx += 1
        else: # two exists
            if nums[i] == nums[one] and nums[i] == nums[two] and two > one: # found second or more duplicates, pass
                continue
            elif nums[i] != nums[one] and nums[i] != nums[two]: # new number
                one = i
                nums[idx] = nums[i]
                # one = i - 1
                idx += 1
            else: # found first duplicate
                two = i
                nums[idx] = nums[i]
                idx += 1
    return idx 
    '''

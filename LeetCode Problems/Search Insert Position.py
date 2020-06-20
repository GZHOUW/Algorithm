'''
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2

Example 2:
    Input: [1,3,5,6], 2
    Output: 1
'''


def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            l = mid + 1

        else: # nums[mid] > target
            r = mid - 1
    print(l)
    print(r)
    return l # if not found, l will be the idx for insert
# ex: [1,2,3,7,8,9] target=5 --> l = 3(7), r=2(3) after loop

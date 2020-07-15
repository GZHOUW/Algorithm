class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        length = len(nums)
        if length == 0:
            return False

        l = 0
        r = length - 1

        while l <= r:
            mid = (r - l)//2 + l # middle position between l and r
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # remove dublicates on the left that are same as mid, e.g. [1,1,3,1,1,1,1] --> [3,1,1,1,1]
                l += 1
            if nums[mid] >= nums[l]: # mid in left portion (if = , then mid is the leftmost)
                if nums[mid] >= target and target >= nums[l]: # target between mid and l
                    r = mid -1
                else:
                    l = mid + 1
            else: # mid in right portion
                if nums[mid] <= target and target <= nums[r]: # target between mid and r
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False

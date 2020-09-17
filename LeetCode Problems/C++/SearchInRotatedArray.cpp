/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.
*/

# include <iostream>
# include <vector>

using namespace std;

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int length = nums.size();
        if (length == 0){
            return false;
        }
        /* Find the separtion point between two parts
          
            1: mid is smaller than right
            2. if mid and right are in the same part, then nums[mid] < nums[right]
            3. Therefore, if nums[mid] > nums[right], m is in left part, r is in right part
        */
        int l = 0;
        int r = length - 1;

        while (l <= r){ 
            int m = (l + r)/2;
            if (nums[m] == target){
                return true;
            }
            if (nums[m] > nums[r]){ // m is in left, r is in right
                if(nums[l] <= target && target < nums[m]) r = m; // target in left
                else l = m + 1;
            }
            else if(nums[m] < nums[r]) {
                if (nums[m]<target && nums[r] >= target) l = m + 1;
                else r = m - 1; 
            }
            else{ // equal --> duplicate
                r --;
            }
        }
        return false;
    }
};
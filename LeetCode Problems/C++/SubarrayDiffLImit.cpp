/*
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
Accepted
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
		if(nums.size()==1) return 1; //corner cases
		
		int curMAX=nums[0];
		int curMIN=nums[0];
		int maxLen=0;
		int left=0;
		for(int right=1; right<nums.size(); right++){
			curMAX=max(curMAX,nums[right]); // current max value in the window
			curMIN=min(curMIN,nums[right]); // current min value in the window
            
			// when nums[right] breaks the window
            if(nums[right]-curMIN>limit || curMAX-nums[right]>limit){
				int temp=right;
				left=temp; // move left to cur position
				curMAX=nums[right];       // reset max value
				curMIN=nums[right];       // reset min value
                
                // iterate from cur towards left until the correct left pos is found
				while (abs(nums[right]-nums[temp])<=limit){
					left=temp;
					temp--;
					curMAX=max(curMAX,nums[left]); // update max value in the new window 
					curMIN=min(curMIN,nums[left]); // update min value in the new window
				}
			}
			maxLen=max(maxLen, right-left+1);
		}
		return maxLen;
	}
};
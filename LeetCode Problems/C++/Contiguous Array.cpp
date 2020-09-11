/*
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
    Input: [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
    Input: [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
    /*
    Algorithm: Traverse through list, if 0 count-1, if 1 count +1
               use map to record the first time a count value occurs, along with its corresponding nums index
               a second (or more) time that count value appear means [first time occur: this time occur] is a valid solution
    */

public:
    int findMaxLength(vector<int>& nums) {
        int count = 0, maxLen = 0;
        unordered_map<int, int> countMap;

        countMap[count] = -1; // for [0,1], when i=1, count=0 and len = i-(-1) = 2
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                count -= 1;
            }
            else {
                count += 1;
            }

            if (countMap.count(count) == 0) { // not in map, 
                countMap[count] = i;
            }
            else {
                // cout << i << ' ' << countMap[i] << endl;
                maxLen = max(maxLen, (i - countMap[count]));
            }
        }
        return maxLen;
    }
};
/*
int main() {
    Solution s = Solution();
    vector<int> nums = { 1,0,0,1,1,1,1,0,0,0,1,0,0 };
    int maxLen = s.findMaxLength(nums);
    cout << maxLen << endl;
}
*/
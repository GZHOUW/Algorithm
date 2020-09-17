/*
Given an array arr[] of integers, find the max difference between any two elements such that larger element appears after the smaller number.
Examples :

Input : arr = {2, 3, 10, 6, 4, 8, 1}
Output : 8
Explanation : The maximum difference is between 10 and 2.

Input : arr = {7, 9, 5, 6, 3, 2}
Output : 2
Explanation : The maximum difference is between 9 and 7.
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution{
public:
    int maxDiff(vector<int> nums){
        int maxDiff = nums[nums.size()-1] - nums[0];
        int min = 0;
        for (int i=1; i<nums.size(); i++){
            int curDiff = nums[i] - nums[min];
            if (curDiff >= maxDiff){ // cur element is greater than max diff, update max diff to cur diff
                maxDiff = curDiff;
            }
            else if (curDiff < 0){ // cur element is less than min, update min to cur
                min = i;
            }
        }
        return maxDiff;
    }
};

int main(){
    Solution s = Solution();
    vector<int> v = {2,3,10,6,4,8};
    int diff = s.maxDiff(v);
    cout << diff;
}
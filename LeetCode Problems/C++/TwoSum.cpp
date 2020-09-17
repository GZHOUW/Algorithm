/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
*/
#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> dict; // key=complement of nums[i], val=idx of nums[i]
	    vector<int> res;

        for (int i = 0; i<nums.size(); i++){
            if (dict.count(nums[i]) == 1){
                res.push_back(dict[nums[i]]);
                res.push_back(i);
                return res;
            }
            else{
                dict[target-nums[i]] = i; 
            }
        }
    }
};

int main(){
    Solution s = Solution();
    vector<int> v = {2, 7, 11, 15};
    int t = 9;
    vector<int> res = s.twoSum(v, t);

    cout<<res[0]<<endl;
    cout<<res[1]<<endl;
    

    return 0;
}
/*
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
The solution set must not contain duplicate triplets.

Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],
    A solution set is:
    [
    [-1, 0, 1],
    [-1, -1, 2]
    ]
*/

#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
Algorithm: 1. Sort the list in ascending order
           2. for every number (a) in the list, do the following:
                2.1. set the number after (a) to be (b) and set the last number to be (c)
                2.2. while (b) is smaller than (c), do the following:
                    2.2.1. if a+b+c=0, return result
                    2.2.2. if too big, move (c) left
                    2.2.3. if too small, move (b) right
                
*/
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());

        for (int one = 0; one < nums.size(); one++){
            int target = -nums[one];
            int two = one + 1;
            int three = nums.size() - 1;

            while (two < three){
                if (nums[two] + nums[three] < target){
                    two ++;
                }
                else if (nums[two] + nums[three] > target){
                    three--;
                }
                else { // Solution found
                    vector<int> sol = {nums[one], nums[two], nums[three]};
                    res.push_back(sol);

                    // ELiminate duplicates for two
                    while (two < three && nums[two]==sol[1]){
                        two ++;
                    }

                    // ELiminate duplicates for one
                    while (two < three && nums[three]==sol[2]){
                        three--;
                    }
                }
            }
             // ELiminate duplicates for one
            while (one+1 < nums.size() && nums[one+1] == nums[one]){
                one ++;
            }
        }
        return res;
    }
};

int main(){
    Solution s = Solution();
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> res = s.threeSum(nums);

    for (int i = 0; i<res.size(); i++){
        for (int j = 0; j<res[0].size(); j++){
            cout<<res[i][j]<<" ";
        }
        cout<<endl;
    }
    

    return 0;
}
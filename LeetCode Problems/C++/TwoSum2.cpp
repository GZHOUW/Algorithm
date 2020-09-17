#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;
        vector<int> res;
        while (left < right){
            if (nums[left] + nums[right] == target){
                res = {left+1, right+1}; // index from 1, not 0
                return res;
            }
            else if (nums[left] + nums[right] > target){
                right --;
            }
            else{
                left ++;
            }
        }
        
        return res;
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
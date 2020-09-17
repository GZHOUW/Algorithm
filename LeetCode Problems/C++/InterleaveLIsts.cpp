#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> interleave(vector<vector<int>>& lists) {
        vector<int> res;
        int i;
        // Create a list that stores the length of each list
        vector<int> length;
        for (i = 0; i < lists.size(); i++){
            length.push_back(lists[i].size());
        }

        // Find out the length of the longest list
        int max_length = 0;
        for (i = 0; i < length.size(); i++){
            if (length[i] > max_length){
                max_length = length[i];
            }
        }

        for (i = 0; i < max_length; i++){
            for (int j = 0; j < lists.size(); j++){
                if (i < length[j]){
                    res.push_back(lists[j][i]);
                }
            }
        }

        return res;
    }
};

int main(){
    vector<vector<int>> l = {{1,4,7},{2,5,8},{3,6,9}};
    Solution s = Solution();
    vector<int> r = s.interleave(l);
    for (int i = 0; i < r.size(); i++){
        cout << r[i];
    }
    return 0;
}
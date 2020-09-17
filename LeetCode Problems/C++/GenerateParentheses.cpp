#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    /*
    Algorithm: start with (, then keep adding ( and )
               if number of ) exceeds (, invalid, return
               if number of either ( or ) exceeds n, invalid, return
               if number of ( and ) both equal to n, valid, append to res
    */
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        generate(res, n, "(", 1, 0);
        return res;
    }
    
    void generate(vector<string> &res, int n, string substring, int nL, int nR){
        if (nL == n && nR == n){
            res.push_back(substring);
            return;
        }
        if (nR > nL || nL > n || nR > n){
            return;
        }
        generate(res, n, substring+"(", nL+1, nR);
        generate(res, n, substring+")", nL, nR+1);
    }
};

int main(){
    Solution s = Solution();
    vector<string> res = s.generateParenthesis(6);
    for (auto i: res)
        cout << i << ' ';
}
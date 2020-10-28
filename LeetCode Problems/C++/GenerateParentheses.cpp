/*Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.*/
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
    
    void generate(vector<string> &res, int n, string substr, int nL, int nR){
        /*
           res: the list of well formed parentheses
           n: number of pairs
           substr: current substring that we are working on
           nL: number of '(' in current substring
           nR: number of ')' in current substring
        */
        if (nL == n && nR == n){ // valid, append
            res.push_back(substr);
            return;
        }
        if (nR > nL || nL > n || nR > n){ // invalid, return
            return;
        }
        generate(res, n, substr+"(", nL+1, nR);
        generate(res, n, substr+")", nL, nR+1);
    }
};

int main(){
    Solution s = Solution();
    vector<string> res = s.generateParenthesis(6);
    for (auto i: res)
        cout << i << ' ';
}

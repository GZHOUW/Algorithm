#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
    /*
    Algorithm:  1. Initialize the triangle with first row
                2. For >=2 rows, row[0] and r[end] are always 1, otherwise row[i] is prevRow[i-1]+prevRow[i]
    */
        vector<vector<int>> triangle;
        if (numRows == 0){
            return triangle;
        }
        vector<int> r = {1};
        triangle.push_back(r);
        
        for (int i = 1; i < numRows; i++){
            vector<int> row;
            for (int j = 0; j<= i; j++){
                if (j == 0 or j == i){
                    row.push_back(1);
                }
                else{
                    row.push_back(triangle[i-1][j-1] + triangle[i-1][j]);
                }
            }
            triangle.push_back(row);
        }
        return triangle;
    }
};

int main(){
    Solution s = Solution();
    int numRow = 3;
    vector<vector<int>> res = s.generate(numRow);

    for (int i = 0; i<res.size(); i++){
        for (int j = 0; j<res[i].size(); j++){
            cout<<res[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
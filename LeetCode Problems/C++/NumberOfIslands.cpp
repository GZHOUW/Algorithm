/*
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    Output: 3
*/
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int totalIslands = 0;
        for (int r = 0; r < grid.size(); r++){
            for (int c = 0; c < grid[0].size(); c++){
               
                if (grid[r][c] == '1'){
                    sinkIsland(grid, r,c);
                    totalIslands++;
                    
                }
            }
        }
        return totalIslands;
    }

    void sinkIsland(vector<vector<char>>& grid, int r, int c){
        //cout<<r<<c<<endl;

        if (0<=r && r<grid.size() && 0<=c && c<grid[0].size()){
            if (grid[r][c]=='1'){
                grid[r][c] = 'x';
            
                sinkIsland(grid, r+1, c);
                sinkIsland(grid, r-1, c);
                sinkIsland(grid, r, c+1);
                sinkIsland(grid, r, c-1);
            }
        }
    }
};
int main() {
  
  Solution s = Solution();
  vector<vector<char>> grid = {{'1','1','1','1','0'},{'1','1','0','1','0'}};
  int x = s.numIslands(grid);
  cout << x<<endl;
  return 0;
}
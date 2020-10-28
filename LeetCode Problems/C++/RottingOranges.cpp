/*In a given grid, each cell can have one of three values:
    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.*/

#include <iostream>
#include <vector>
#include <deque>
using namespace std;


class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        deque<vector<int>> rotten;
        int freshCount, rottenCount, r, c, i, j, x, y;
        vector<vector<int>> neighbor;
        int time = 0;
        
        for (r=0; r<grid.size(); r++){
            for (c=0; c<grid[0].size(); c++){
                if (grid[r][c] == 2){
                    rotten.push_back(vector<int> {r,c});
                }
                else if (grid[r][c] == 1){
                    freshCount ++;
                }
            }
        }
        
        cout<<freshCount<<endl;
        while (freshCount > 0 && !rotten.empty()){
            
            rottenCount = rotten.size();
            for (i = 0; i<rottenCount; i++){
                vector<int> coord = rotten[0];
                rotten.pop_front();
                r = coord[0];
                c = coord[1];
                grid[r][c] = 2;
                neighbor = {{r-1,c}, {r+1,c},{r,c+1},{r,c-1}};
                for (j=0; j<neighbor.size(); j++){
                    x = neighbor[j][0];
                    y = neighbor[j][1];

                    if (0<=x && x<grid.size() && 0<=y && y<grid[0].size() && grid[x][y]==1){
                        grid[x][y] = 2;
                        freshCount --;
                        rotten.push_back(neighbor[j]);
                    }
                }
            }
            time ++;
        }
        
        //cout << freshCount<<endl;
        if (freshCount == 0){
          return time;  
        }
        else{
            return -1;
        }
        
    }
};

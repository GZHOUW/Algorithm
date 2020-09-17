/*
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Return the max amout of water.
*/
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int cur_area;
        int max_area = 0;
        while (left < right){
            cur_area = (right - left) * min(height[left], height[right]);
            max_area = max(max_area, cur_area);

            // keep the longer bar and move the shorter bar inwards
            if (height[left] < height[right]){
                left ++;
            }
            else{
                right--;
            }
        }
        return max_area;
    }
};
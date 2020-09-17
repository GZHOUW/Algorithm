#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
Algorithm: Find a partition point in x and another in y that divides x and y into x1,x2, y1,y2
           such that len(x1)+len(y1) = len(x2)+len(y2) and x1[-1] < y2[0] and y1[-1] < x2[0]
           then median is max(x1[-1], y1[-1]) if odd or mean(max(x1[-1], y1[-1]), min(x2[0], y2[0])) if even

Ex: x = [1,3,8,9,15], y = [7,11,18,19,21,25]
    x1 = [1,3,8,9] | x2 = [15]
    y1 = [7]       | y2 = [11,18,19,21,25]
*/
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double res;
        // Binary search must be performed on the shorter array, hence swap num1 and num2 is num1 is larger
        int len1 = nums1.size();
        int len2 = nums2.size();
        if (len1 > len2){
            return findMedianSortedArrays(nums2, nums1);
        }

        // Perform binary search on nums1 
        int left = 0;
        int right = nums1.size();
        int part1, part2; // x1 contains all elements BEFORE x[part1], y1 contains all elements BEFORE y[part2]
        int maxLeft1, minRight1, maxLeft2, minRight2;
        
        while (left <= right){
            part1 = (left + right)/2; // or (right-left)/2 + left
            part2 = (len1 + len2 + 1)/2 - part1;
            cout << part1 << endl;

            maxLeft1 = (part1 == 0) ? INT32_MIN: nums1[part1-1];
            minRight1 = (part1 == len1) ? INT32_MAX: nums1[part1];
            maxLeft2 = (part2 == 0) ? INT32_MIN: nums2[part2-1];
            minRight2 = (part2 == len2) ? INT32_MAX: nums2[part2];

            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1){
                //found
                if ((len1 + len2)%2 == 0){ // even
                    
                    res = (max(maxLeft1, maxLeft2) + min(minRight1, minRight2))/2.0;
                    return res;
                }
                else{
                    res = max(maxLeft1, maxLeft2);
                    return res;
                }
            }
            else if (maxLeft1 > minRight2){ // part1 need to go left
                right = part1 - 1;
            }
            else{ // part1 need to go right
                left = part1 + 1;
            }
        }
    }
};

int main(){
    Solution s = Solution();
    vector<int> x = {1,2,3,4,5};
    vector<int> y = {10,11,12,13};
    double median = s.findMedianSortedArrays(x, y);
    cout << median;
}
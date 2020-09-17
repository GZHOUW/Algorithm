#include <bits/stdc++.h>

using namespace std;

// Complete the hourglassSum function below.
int hourglassSum(vector<vector<int>> arr) {
    int maxSum = INT32_MIN;
    int curSum;
    
    for (int r = 1; r <= 4; r++){
        for (int c = 1; c <=4; c++){
            curSum = arr[r-1][c-1]+arr[r-1][c]+arr[r-1][c+1]+arr[r][c]+arr[r+1][c-1]+arr[r+1][c]+arr[r+1][c+1];
            maxSum = max(maxSum, curSum);
        }
    }
    return maxSum;
}

int main()
{

    vector<vector<int>> arr(6);
    for (int i = 0; i < 6; i++) {
        arr[i].resize(6);
        for (int j = 0; j < 6; j++) {
            arr[i][j] = i+j;
        }
    }

    int result = hourglassSum(arr);
    cout << result;
    return 0;
}

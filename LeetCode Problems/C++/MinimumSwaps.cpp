#include <bits/stdc++.h>

using namespace std;

int minimumSwaps(vector<int> arr) {
    int swap = 0;
    for (int i = 0; i < arr.size(); i++){
        
        if (arr[i] != i+1){// not at right pos, make swap
            int temp = arr[arr[i]-1]; // the number that is taking curNum's pos
            arr[arr[i]-1] = arr[i];
            arr[i] = temp;
            swap ++;
            i--; // for [4,3,1,2], if dont decrement i, becomes [2,1,3,4]
                 // need to make sure arr[i] has the right number before leaving
        }
    }
    return swap;
}

void swap(vector<int> &arr, int x, int y) {
    int temp = arr[y]; // the number that is taking curNum's pos
    arr[y] = arr[x];
    arr[x] = temp;
}

int main(){
    vector<int> arr = {1,2,3,4,5,6};
    swap(arr, 1,4);
    cout<<arr[1]<<endl;

    int val = 1024;
    int& ref = val;
    ref = 444;
    cout << ref << endl;

    arr = {9,9,9};
    vector<int> arr2 = arr;
    arr[1] = 1000;
    cout << arr[1];
    cout << arr2[1];
}
#include <iostream>
#include <vector>
using namespace std;

class QuickSort{
public:
/*
Algorithm: 1. if len <= 1, return (already sorted)
           2. choose a pivot randomly
           3. partition the array around pivot (put pivot in correct (sorted) position, put all elements
              smaller than pivot on the left of pivot, put all elements greater than pivot on the right
              of pivot)
           4. Recursively quickSort the sub-array that is on the left of pivot
           5. Recursively quickSort the sub-array that is on the right of pivot
*/
void sort(vector<int> &arr, int left, int right){
    if (left >= right){ // arr is length 0 or 1
        return;
    }
    int pivot = choosePivot(arr, left, right);
    swap(arr[left], arr[pivot]); // put hte pivot in the beginning for now

    int pivot_correct_pos = partition(arr, left, right); // left is now pivot

    sort(arr, left, pivot_correct_pos-1);
    sort(arr, pivot_correct_pos+1, right);
}

int partition(vector<int> &arr, int left, int right){
    int pivot = left; // swapped before hand
    int separate = left + 1; // separation between the elements that are smaller and larger than pivot

    for (int i = left+1; i <= right; i++){
        if (arr[i] < arr[pivot]){
            swap(arr[i], arr[separate]);
            separate ++;
        }
        // dont need to do anything to the ones larger, bc they will stay on right side
    }
    swap(arr[pivot], arr[separate-1]); // place pivot in the right position
    return separate-1;
}

int choosePivot(vector<int> arr, int left, int right){
    srand (time(NULL));
    int pivot = rand() % (right-left+1) + left;
    return pivot;
}
};

int main(){
    QuickSort s = QuickSort();
    vector<int> arr = {3,6,5,1,9,10,2,7,4,8};
    s.sort(arr, 0, arr.size()-1);
    for (int i =0; i<arr.size(); i++){
        cout<<arr[i]<<endl;
    }
}
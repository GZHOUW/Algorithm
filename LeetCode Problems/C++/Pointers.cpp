# include <iostream>
# include <vector>
# include <memory>
using namespace std;

class PointerFcns{
public:

// Take an int pointer as argument and double the value it points to
void doubleNum(int* ptr){
    *ptr *= 2; // Dereferrence the pointer and multiply by 2
}


// Take an array pointer as argument and print the values in the array
void printArray(int* ptr, int size){
    for (int i = 0; i<size; i++){
        cout << *ptr << endl;
        ptr ++;
    }
}


void printArray2(){
    int arr[8] = {1,2,3,4,5,6,7,8};
    int* ptr = arr;
    
    // Both pointers point to the first element
    while (ptr <= &arr[7]){ // compare pointer: 1st element address < 2nd element address
        cout << *ptr << endl;
        ptr ++;
    }
    cout << "Print backwards"<<endl;
    // Print again backwards, now ptr points at one space AFTER last element
    while (ptr > arr){ // arr still points at first elment
        ptr --;
        cout << *ptr << endl;
    }
}

void getLength(){
    int array[] = {1,2,3,4,5,6};

    cout << array <<endl; // a pointer to the first element of the array
    cout << array+1<<endl; // a pointer to the second element of the array

    // both “array” and “&array” are printing same address, but they are DIFFERENT TYPE of addresses
    cout << array <<endl;
    cout << &array << endl; // a pointer to whole array, therefore *(&array+1) is lication after the last element of array

    // get size
    int arraySize = *(&array + 1) - array;
    cout << "Length of array is: "<< arraySize << endl;
}

void dynamicAllocation(){
    int* ptr = nullptr;
    ptr = new int[100];// allocate memory for a new int array
    for (int i = 0; i < 100; i++){// store value 1 in each element
        ptr[i] = 1; // directly use subscript to access
    }
    // release the allocated memory for future use
    delete [] ptr;

}

int* duplicateArr(const int* arr, int size){
    int* newArr = nullptr;

    //Allocate a new array
    newArr = new int[size];

    // Copy elements into newArr
    for (int i = 0; i<size; i++){
        newArr[i] = arr[i];
    }

    // Return a pointer to the new array
    return newArr;
}
};


int main(){
    PointerFcns p = PointerFcns();

    // doubleNum
    int x = 5;
    cout << "Running doubleSum"<<endl;
    p.doubleNum(&x);
    cout << x << endl;

    // Array fcnsS
    int array[] = {1,2,3,4,5,6};
    
    // getLength
    cout << "Running getLength"<<endl;
    p.getLength();

    // printArray
    cout << "Running printArray"<<endl;
    p.printArray(array, 6);

    // printArray2
    cout <<"Running printArray2"<<endl;
    p.printArray2();

    cout << "Running dymanicAllocation"<<endl;
    p.dynamicAllocation();

    cout << "Running duplicateArr"<<endl;;
    int* newArr = p.duplicateArr(array, 6);
    cout << newArr[1];
}
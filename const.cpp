#include <iostream>
#include <vector>
using namespace std;

int main(){
    // 1. non-const ref refer to non-const object ---- VALID
    int x = 2;
    int& r1 = x;

    // 2. const ref refer to const object ---- VALID    
    const int n = 100;
    const int& r2 = n;
    const int& r3 = 9999; // 9999 is a const object
    
    // 3, const ref refer to non-const object ---- VALID
    int y = 42;
    const int& r4 = y;

    // 4. non-const ref refer to const object ---- ERROR
    const int z = 3;
    // int &r5 = z; ERROR


    // const pointer
    int a = 9;
    int* const p1 = &a; // same as const int* p1 = &a;
    cout << *p1;







    return 0;
}
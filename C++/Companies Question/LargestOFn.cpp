#include<iostream>
#include<bits/stdc++.h>
using namespace std;
class FindMax{

    public:
    int maxNum(int array[],int size){
    int temp = array[0];
    // int size=sizeof(array)/sizeof(int);
    for (int i = 0; i <size ; i++) {
    if (array[i] > temp){
        temp = array[i];
    }
    }
    return temp;
    }
};
int main(){
   FindMax FindMaxArray;
    int n;
    cout<<"Enter the number of ele array";
    cin>>n;
    cout << "Program to determine maximum number in Array." << endl << endl;
    int a[n];
    for(int i = 0; i < n; ++i)
    {
       cout << "Enter Number " << i + 1 << " : ";
       cin >> a[i];
    }
    cout << "The largest value is: " << FindMaxArray.maxNum(a,n) << endl;

    return 0;   
}
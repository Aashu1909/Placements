#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int Max_sum_subset(int *arr,int n){
     int smallest = -10000, largest = 0;
    for(int i=0; i<n; i++){
        largest = largest + arr[i];
        if(smallest < largest)
            smallest = largest;
        if(largest < 0)
                largest = 0;
    }
    return smallest;
}

int main(){
    int arr_1[]={-1,-2,-3,5};
    int n1=sizeof(arr_1)/sizeof(int);
    cout<<endl;
    cout<<"Array 1 Before: ";
    for(int i=0;i<n1;i++){
        cout<<arr_1[i]<<" ";
    }
    cout<<endl;
    cout<<Max_sum_subset(arr_1,n1);
}
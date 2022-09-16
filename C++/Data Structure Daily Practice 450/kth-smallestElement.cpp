#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void Kth_smallest(int arr[],int n,int k1){
    sort(arr,arr+n);
    cout<<arr[k1-1]<<" ";
}

int main(){
    int arr_1[]={7, 10, 4, 3, 20, 15};
    int n1=sizeof(arr_1)/sizeof(int);
    int k;
    cout<<"Enter K: ";
    cin>>k;
    cout<<endl;
    cout<<"Array 1 Before: ";
    for(int i=0;i<n1;i++){
        cout<<arr_1[i]<<" ";
    }
    cout<<endl;
    Kth_smallest(arr_1,n1,k);
}
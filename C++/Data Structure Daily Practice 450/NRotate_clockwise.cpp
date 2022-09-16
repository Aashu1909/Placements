#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void N_rotate(int arr[],int n,int r){
    
    int temp[r];
    if (n>r){
        int index=0;
        for(int i=n-r;i<n;i++){
            temp[index]=arr[i];
            index++;
        }
        // Now shifting the values
        for(int i=n-1;i>=r;i--){
            arr[i]=arr[i-r];
         }
        // now adding element from the back
        for(int i =0 ;i<r ;i++){
            arr[i]=temp[i];
        }
    }
    cout<<"Array after rotation:";
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";

    }
    cout<<endl;
}

int main(){
    int arr_1[]={7, 10, 4, 3, 20, 15};
    int n1=sizeof(arr_1)/sizeof(int);
    int k;
    cout<<"Enter Rotation times: ";
    cin>>k;
    cout<<endl;
    cout<<"Array 1 Before: ";
    for(int i=0;i<n1;i++){
        cout<<arr_1[i]<<" ";
    }
    cout<<endl;
    N_rotate(arr_1,n1,k);
}
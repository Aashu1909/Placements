#include <iostream>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;
    
/* 
here the idea is 
if the element in an array is zero
swap it with the next non zero element
*/
// Complexity O(n^2)
void move_zeros(int arr[],int size){
    for(int i=0;i<size;i++){
        if(arr[i]==0){
            for(int j=i+1;j<size;j++){
                if(arr[j]!=0){
                    int temp=arr[j];
                    arr[j]=arr[i];
                    arr[i]=temp;
                }
            }
        }
    }
}

int main() {

    int arr[]={10,5,0,0,8,0,9,0};
    int size=sizeof(arr)/sizeof(int);
    cout<<"Before solution:"<<endl;
    for(int i=0;i<size;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    move_zeros(arr,size);
    cout<<"Solution: "<<endl;
    for(int i=0;i<size;i++){
        cout<<arr[i]<<" ";
    }
    return -1;
}
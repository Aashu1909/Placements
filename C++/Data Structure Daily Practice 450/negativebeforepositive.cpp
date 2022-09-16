#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void solution(int arr1[],int len){
    int i=0,j=len-1;
    while(i<=j){
        //both negative
        if(arr1[i]<0 and arr1[j]<0){
            i++;
        }
        //i positive and j negative
        else if(arr1[i]>0 and arr1[j]<0){
            swap(arr1[i],arr1[j]);
            i++;
            j--;
        }
        //both positive
        else if(arr1[i]>0 and arr1[j]>0){
            j--;
        }
        // j positive and i negative
        else{
            i++;
            j--;
        }
        
        
    }
    cout<<"After Change 1: ";
    for(int k =0;k<len;k++){
        cout<<arr1[k]<<" ";
    }
    cout<<endl;
}
void arrange(int *arr,int n){
    int i,index;
    index=0;
    for(i=0;i<n;i++){
        if(arr[i]<0 ){
            if(i!=index){
            int temp=arr[i];
            arr[i]=arr[index];
            arr[index]=temp;
        }
          index++;
        }

    }
    cout<<"After change 2:\n";
    for(int k =0;k<n;k++){
        cout<<arr[k]<<" ";
    }
    cout<<endl;
}
int main(){

    int arr[]={1,2,3,4,-15,-45,-78,-56,-54};
    int n=sizeof(arr)/sizeof(int);
    cout<<"Array Before:";
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    solution(arr,n);
    arrange(arr,n);
}
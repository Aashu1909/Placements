#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void Sort(int arr[],int n){
    int count[3]={0};
    for(int i=0;i<n;i++){
        count[arr[i]]+=1;
    }
    int index=0;
    for(int j=0;j<3;j++){
        while(count[j]>0){
            arr[index]=j;
            index++;
            count[j]-=1; 
        }
    }
    cout<<"Array 1 after: ";
    for(int k=0;k<n;k++){
        cout<<arr[k]<<" ";
    }
}

int main(){
    int arr_1[]={0,1,0,0,1,2,2};
    int n1=sizeof(arr_1)/sizeof(int);
    cout<<"Array 1 Before: ";
    for(int i=0;i<n1;i++){
        cout<<arr_1[i]<<" ";
    }
    cout<<endl;
    Sort(arr_1,n1);
}
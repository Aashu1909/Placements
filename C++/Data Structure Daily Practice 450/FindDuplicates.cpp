#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void find_duplicate(int num[],int n){
    int duplicate=-1;
    int curr;
    for(int i=0;i<n;i++){
        curr=abs(num[i]);
        
        if (num[curr]<0){
            duplicate=curr;
            break;
        }
        num[curr]*=-1;
        
    }
    cout<<"Duplicate Num is:"<<curr;
}

int main(){
    int arr_1[]={1,1,2};
    int n1=sizeof(arr_1)/sizeof(int);
    cout<<endl;
    cout<<"Array 1 Before: ";
    for(int i=0;i<n1;i++){
        cout<<arr_1[i]<<" ";
    }
    cout<<endl;
    find_duplicate(arr_1,n1);
}
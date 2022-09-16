#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void Max_sum_subset(int *arr,int n){
    int res=INT_MIN;
    for(int i=0;i<n;i++){
        int sum=0;
        for(int j=0;j<=i;j++){
            sum+=arr[j];
            cout<<arr[j]<<" ";
        }
        cout<<endl;
        res=max(res,sum);
    }
    cout<<"Maximum Sub Array Sum:"<<res;

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
    Max_sum_subset(arr_1,n1);
}
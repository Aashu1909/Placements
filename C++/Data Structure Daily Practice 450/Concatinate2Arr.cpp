#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int temp[100];//global
void merge(int arr1[],int arr2[],int l1,int l2){

    int i=0;
    while (i<l1)
    {
        /* code */
        if(arr1[i]==arr2[0]){
            i++;
        }
        else if(arr1[i]<arr2[0]){
            swap(arr1[i],arr2[0]);
            sort(arr2,arr2+l2);
            i++;
        }
        else if(arr1[i]>arr2[0]){
            swap(arr2[0],arr1[i]);
            sort(arr2,arr2+l2);
            i++;
        }
    }

    for(int k=0;k<l1;k++){
        cout<<arr1[k]<<" ";
    }
    for(int l=0;l<l2;l++){
        cout<<arr2[l]<<" ";
    }
    cout<<endl;
}

int main(){

    int arr_1[]={10,20,30,40,50};
    int arr_2[]={9,11,33,45,66};

    int n1=sizeof(arr_1)/sizeof(int);
    int n2=sizeof(arr_2)/sizeof(int);
    cout<<"Array 1 Before: ";
    for(int i=0;i<n1;i++){
        cout<<arr_1[i]<<" ";
    }
    cout<<endl;
    cout<<"Array 2 Before: ";
        for(int i=0;i<n2;i++){
        cout<<arr_2[i]<<" ";
    }
    cout<<endl;
    merge(arr_1,arr_2,n1,n2);
    // union_in_array(arr_1,arr_2,n1,n2);   
}
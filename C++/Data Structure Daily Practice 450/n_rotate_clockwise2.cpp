#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void N_rotate(int arr[],int n,int r){    
    int rotation=r%n;
   while (rotaion>0)
   {
       /* code */
       int last_elem=arr[n-1];
       for(int i=n-1;i>=0;i--){
           arr[i]=arr[i-1];
       }
       arr[0]=last_elem;
       rotation--;
   }
    cout<<"Array after rotation:";
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main(){
    int arr_1[]={1,2,3,4,5};
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
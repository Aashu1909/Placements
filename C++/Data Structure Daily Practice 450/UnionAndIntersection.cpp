#include<iostream>
#include<bits/stdc++.h>
using namespace std;
struct pair
{
    /* data */
    int intersection;
    int union_1; 
};

void Union_intersection_in_array(int arr1[],int arr2[],int l1,int l2){

int temp[100];//array to store the comman elements.
int index=0;
int size=0;//variabloe to determine size of resulting temp array.
int i=0,j=0;// loop variables for arr1 and arr2 respectively
while (i<l1 and j<l2)
{
    /* code */
    if(arr1[i]==arr2[j]){
        size+=1;
        temp[index]=arr1[i];
        i++;
        j++;
        index++;
    }
    else if(arr1[i]>arr2[j]){
        j++;
    }
    else if (arr2[j]>arr1[i]){
        i++;
    }
}
cout<<"Count for intersection. "<<size<<endl;
int union_no;
union_no=l1+l2-size;
cout<<"union element count:"<<union_no;
cout<<endl;
}
int main(){

    int arr_1[]={4,6,9,10,15,18,20};
    int arr_2[]={4,5,9,12,15,19,20};

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
    Union_intersection_in_array(arr_1,arr_2,n1,n2);
    // union_in_array(arr_1,arr_2,n1,n2);
    
}
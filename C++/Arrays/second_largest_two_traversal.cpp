#include <iostream>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;
    
int Largest_element(int arr[],int size){
    int largest=INT_MIN;
    for(int i=0;i<size;i++){
        if (arr[i]>largest){
            largest=arr[i];
        }
    }
    return largest;
}
int second_largest(int arr[],int size){
    int largest_element=Largest_element(arr,size);
    int second_largest=INT_MIN;
    for(int i =0;i<size;i++){
        if(arr[i]!=largest_element){
            if (arr[i]>second_largest){
                second_largest=arr[i];
            }
        }
    }
    return second_largest;
}


int main() {
    int arr[5]={5,3,7,10,2};
    cout<<second_largest(arr,5);
    return -1;

}
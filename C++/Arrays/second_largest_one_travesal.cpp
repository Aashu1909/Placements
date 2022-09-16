#include <iostream>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;
    
int second_largest(int arr[],int size){
    int largest=INT_MIN;
    int second_largest=INT_MIN;
    for(int i =0;i<size;i++){
        if(arr[i]>largest){
            second_largest=largest;
            largest=arr[i];
        }
        else if(arr[i]>largest){
            if(second_largest==INT_MIN ||arr[i]>second_largest){
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
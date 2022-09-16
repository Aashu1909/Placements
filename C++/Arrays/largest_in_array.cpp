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


int main() {
    int arr[5]={5,3,7,10,2};
    cout<<Largest_element(arr,5);
    return -1;

}
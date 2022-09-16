#include<iostream>
#include<bits/stdc++.h>
using namespace std;
// int sortarr[];
void minheapify(int arr[],int size,int i){
    int leftInd=2*i+1;
    int rightInd=2*i+2;
    int smallest=i;
    if(leftInd<size&&arr[smallest]>arr[leftInd]){
        smallest=leftInd;
    }
    if(rightInd<size&&arr[smallest]>arr[rightInd]){
        smallest=rightInd;
    }
    if(smallest!=i){
        swap(arr[smallest],arr[i]);
        minheapify(arr,size,smallest);
    }
}
void buildHeap(int arr[],int n ){
    for(int i=n-2/2;i>=0;i--){
        minheapify(arr,n,i);
    }
}

void Heapsort(int arr[],int n ){
    buildHeap(arr,n);
    int heapsize=n;
    for(int i=n-1;i>=1;i--){
        swap(arr[0],arr[i]);
        heapsize--;
        minheapify(arr,heapsize,0);
        
    }
}


void printArray(int arr[],int n){
    for(int i =0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}


int main() 
{ 
	int arr[] = {150,12,13,24,31,54,45,65,4,8,78,79,75,2,42,35,65,23,213213211}; 
	int n = sizeof(arr)/sizeof(arr[0]); 

	Heapsort(arr, n); 

	cout << "Sorted array is \n"; 
	printArray(arr, n); 
} 
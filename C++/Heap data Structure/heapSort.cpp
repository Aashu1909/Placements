#include<iostream>
#include<bits/stdc++.h>
using namespace std;

void Maxheapify(int arr[],int size,int i){
  int leftIndex=2*i+1;
  int rightIndex=2*i+2;
  int largestEle=i;
  if(leftIndex<size &&arr[largestEle]<arr[leftIndex]){
      largestEle=leftIndex;
  }
  
  if(rightIndex<size &&arr[largestEle]<arr[rightIndex]){
      largestEle=rightIndex;
  }

  if(largestEle!=i){
      swap(arr[largestEle],arr[i]);
      Maxheapify(arr,size,largestEle);
  }
}


void buildHeap(int arr[],int n){
    for(int i=n-2/2;i>=0;i--){
        Maxheapify(arr,n,i);
    }
}
void Heapsort(int arr[],int n){
    buildHeap(arr,n);
    int heapsize=n;
    for(int i=n-1;i>=1;i--){
        swap(arr[0],arr[i]);
        heapsize--;
        Maxheapify(arr,heapsize,0);
    }
}


void printArray(int arr[],int n){
    for(int i=0;i<n;i++){
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
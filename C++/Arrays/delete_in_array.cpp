#include <iostream>
#include <cmath>
using namespace std;

int delete_element(int arr[], int n, int x){
    // Firstly Searching the element that is to be deleted
    int i;
    for(i =0;i<n;i++){
        if(arr[i]==x){
            break;
        }
    }
    if(i==n){
        return n;
    }
    for (int j=i;j<n-1;j++){
        arr[j]=arr[j+1];
    }
    return n-1;        
} 


    
int main() {
	
       int arr[5]={6,10,5,3,2};
       int n =5;
       cout<<"Before Deletion"<<endl;
       for(int i=0; i < n; i++)
       {
       	cout<<arr[i]<<" ";
       }
       cout<<endl;
       int x = 5;
       n = delete_element(arr, n, x);
       cout<<"After Deletion"<<endl;
       for(int i=0; i < n; i++)
       {
       		cout<<arr[i]<<" ";
       }
    
}
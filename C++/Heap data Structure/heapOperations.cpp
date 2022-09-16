#include<iostream>
#include<bits/stdc++.h>
using namespace std;
class MinHeap{
    public:
    int *arrMin;
    int sizeMin;
    int capacityMin;
    MinHeap(int cap){
        arrMin=new int[c];
        sizeMin=0;
        capacityMin=c;
    }

    int leftMIN(int i){
        return 2*i+1;
    }
    int rightMIN(int i){
        return 2*i+2;
    }
    int parentMIN(int i){
        return (i-1)/2;
    }
    void insertMIN(int);
    void DeleteMIN(int);
};
void MinHeap::insertMIN(int x){
    if (sizeMin==capacityMin) return ;
    sizeMin++;
    arrMin[sizeMin-1]=x;
    for(int i=sizeMin-1;i!=0&&arr[parentMIN(i)]>arrMin[i]){
        swap(arrMin[parentMIN(i)],arrMin[i]);
        i=parentMIN(i);
    }
}


class MaxHeap{
    public:
    int *arr;
    int size;
    int capacity;
    MaxHeap(int c){
        arr=new int[c];
        size=0;
        capacity=c;
    }

    int MaxHeapleft(int i){
        return 2*i+1;
    }
    int MaxHeapright(int i){
        return 2*i+2;
    }
    int MaxheapParent(int i){
        return (i-1)/2;
    }
    void Maxinsert(int);
    void MinDelete(int);
};
   



int main(){
    MinHeap m1;
    m1.insertMIN(10)
}
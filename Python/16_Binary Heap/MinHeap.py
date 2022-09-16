# MIN HEAP
# Complete Binary Tree
# Every Node has Value lesser than its dessendents 
# Means every node is smaller than its children.
from cgitb import small
import math
class MinHeap:
    def __init__(self):
        self.arr=list()
    
    def parent(self,i):
        return (i-1)//2
    
    def leftChild(self,i):
        return (2*i)+1
        
    def rightChild(self,i):
        return (2*i)+2
    
    # O(log(n)) Time Complexity
    def insert(self,data):
        self.arr.append(data)
        i=len(self.arr)-1
        while i>0 and self.arr[self.parent(i)]>self.arr[i]:
            p=self.parent(i)
            self.arr[i],self.arr[p]=self.arr[p],self.arr[i]     #SWAP WITH PARENT
            i=p

    # Min heapify function will fix the tree
    def minHeapify(self,index):
        leftChild=self.leftChild(index)
        rightChild=self.rightChild(index)
        smallest=index
        n=len(self.arr)
        if leftChild<n and self.arr[leftChild]<self.arr[smallest]:
            smallest=leftChild
        if rightChild<n and self.arr[rightChild]<self.arr[smallest]:
            smallest=rightChild
        if smallest!=index:
            self.arr[smallest],self.arr[index]=self.arr[index],self.arr[smallest]
            self.minHeapify(smallest)

    # Extract Min operation removes the minimum in the BinaryHeap
    def ExtractMin(self):
        n=len(self.arr)
        if n==0:
            return math.inf
        res=self.arr[0]
        self.arr[0]=self.arr[n-1]
        self.arr.pop()
        self.minHeapify(0)
        return res

    def decreaseKey(self, i, x):
        arr = self.arr
        arr[i] = x

        while i != 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]

            i = p

    def delete(self, i):
        n = len(self.arr)

        if i >= n:
            return

        else:
            self.decreaseKey(i, -math.inf)
            self.extractMin()

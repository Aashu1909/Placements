class MaxHeap:
    def __init__(self,cap):
        self.capacity=cap
        self.arr=[0]*self.capacity
        self.size=0

    def left_child(self,index):
        return (2*index+1)
    def right_child(self,index):
        return (2*index+2)
    def parent(self,index):
        return (index-1)//2
    def has_left_child(self,index):
        return self.left_child(index) < self.size
    def has_right_child(self,index):
        return self.right_child(index)<self.size
    def has_parent(self,index):
        return self.parent(index)>=0
    def is_full(self):
        return self.size==self.capacity

    def insert(self,data):
        print(self.size,self.capacity)
        if self.is_full():
            raise('Heap is Full')
        self.arr[self.size]=data
        self.size+=1
        self.heapifyUp()

    def swap(self,index1,index2):
        temp=self.arr[index1]
        self.arr[index1]=self.arr[index2]
        self.arr[index2]=temp

    def heapifyUp(self):
        index=self.size-1
        while ( self.has_parent(index) ) and (self.arr[self.parent(index)] < self.arr[index]):
            self.swap(self.parent(index),index)
            index=self.parent(index)

    def heapifyDown(self):
        index=0
        while (self.has_left_child(index)):
            larger_child_index=self.left_child(index)
            if  (self.has_right_child(index)) and (self.arr[larger_child_index] < self.arr[self.right_child(index)]):
                larger_child_index=self.right_child(index)
            if self.arr[index]>self.arr[larger_child_index]:
                break
            else:
                self.swap(larger_child_index,index)
            index=larger_child_index 
    
    def remove(self):
        if self.size==0:
            raise('Heap is Empty')
        data=self.arr[0]
        self.arr[0]=self.arr[self.size-1]
        self.size-=1
        self.heapifyDown()
        return data            

    def print(self):
        print(self.arr)

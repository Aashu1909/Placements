class MinHeap:
    def __init__(self,capacity):
        self.arr=[0]*capacity
        self.size=0
        self.capcity=capacity
    
    def left(self,index):
        return (2*index+1)
    
    def right(self,index):
        return (2*index+2)
    
    def parent(self,index):
        return (index-1)//2

    def has_parent(self,index):
        return self.parent(index)>=0
    
    def has_left_child(self,index):
        return self.left(index)<=self.size
    
    def has_right_child(self,index):
        return self.right(index)<=self.size

    def isFull(self):
        return self.size==self.capcity
    
    def get_minimum(self):
        return self.arr[0]
    # Iterative heapify Up O(logn)  O(1) aux space
    def heapifyUp(self):
        index=self.size-1
        while (self.has_parent(index)) and ( self.arr[self.parent(index)] > self.arr[index] ):
            self.swap( self.parent(index), index  )
            index=self.parent(index)
           
    def heapify_recursive(self,index):
        if (self.has_parent(index)) and (self.arr[self.parent(index)] > self.arr[index]):
            self.swap(self.arr[self.parent(index)],self.arr[index])
            self.heapify_recursive(self.parent(index))

    def swap(self,index1,index2):
        temp=self.arr[index1]
        self.arr[index1]=self.arr[index2]
        self.arr[index2]=temp

    def insert(self,data):
        if self.isFull():
            raise('HEAP IS FULL')
        self.arr[self.size]=data
        self.size+=1
        self.heapifyUp()
    
    def remove(self):
        if (self.size==0):
            raise("Empty Heap")
        data=self.arr[0]
        self.arr[0]=self.arr[self.size-1]
        self.size-=1
        self.heapifyDown()
        self.arr[-1]=0
        return data
   
    '''
    Steps for heapify down
    1 intialise index=0
    2 check if index has left child or not beacuse we fill a binary heap from left to right so its important to check for its 
        completeness
    3 start a while loop till index has a left child 
    4 within a while initilise a smaller_child_index as left child index of root index
    5 if left child index is greater than right child index
        change the smaller child index to right child index of the root
    6 if arr[index] is lesser than the smaller child index break from the loop 
        else swap there values 
    7 change the index to smaller child index
    8 repeat this step until we created a minheap
    '''
    
    def heapifyDown(self):  
        index=0
        while (self.has_left_child(index)):
            
            smaller_Child_Index=self.left(index)
            # Right index element is SMALLER than left index Element
            if (self.has_right_child(index)) and ( self.arr[self.right(index)] < self.arr[self.left(index)] ):
                smaller_Child_Index=self.right(index)
            
            if (self.arr[index] < self.arr[smaller_Child_Index] ):
                break
            else:
                self.swap(index,smaller_Child_Index)
            index=smaller_Child_Index        

    def print_heap(self):
        print(self.arr)


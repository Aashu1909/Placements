# Implementing deque using a circular array to optimize the insertFront and DeleteFront operation
from selectors import EpollSelector


class MyDeque:
    def __init__(self,capacity) -> None:
        self.front=0
        self.sz=0
        self.capacity=capacity
        self.arr=[None]*self.capacity

    def insertRear(self,data):
        if self.sz==self.capacity:
            return 
        rear=(self.front+self.sz-1)%self.capacity
        self.arr[rear]=data
        self.sz+=1

    def insertFront(self,data):
        if self.sz==self.capacity:
            return 
        self.front=(self.front-1)%self.capacity
        self.arr[self.front]=data
        self.sz+=1
    
    def deleteFront(self):
        if self.sz==0:
            return 
        else:
            res=self.arr[self.front]
            self.front=(self.front+1)%self.capacity
            self.sz-=1
        return res
    
    def deleteRear(self):
        if self.sz==0:
            return 
        else:
            rear=(self.front+self.sz-1)%self.capacity
            res=self.arr[rear]
            self.sz-=1
        return res

    def getFront(self):
        return self.arr[0]

    def getReae(self):
        return self.arr[-1]
        
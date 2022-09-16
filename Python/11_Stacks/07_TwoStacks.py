# Implementation of two stack in an array/List
"""The first method for implementing Two stack in an array is to divide the array into Two
Equal half and store the value of the stack
This results in inefficient use of the space 
"""
class TwoStacks:
    def __init__(self,n):
        self.sz=n       
        self.arr=[None]*n
        self.top1=(self.sz-1)//2
        self.top2=(self.sz)//2
        print('Top1',self.top1,'top2',self.top2)
    
    # Method to push element in stack1
    def push1(self,x):
        if self.top1>0:
            self.arr[self.top1]=x
            self.top1-=1
        else:
            print('Stack1 overflow')
    
    def push2(self,x):
        if self.top2<self.sz:
            self.arr[self.top2]=x
            self.top2+=1
        else:
            print('Stack2 Overflow')
    
    def pop1(self):
        if self.top1 <= self.sz/2:
            x=self.arr[self.top1]
            self.arr[self.top1]=None
            self.top1+=1
            return x
        else:
            print('Stack1 Underflow')
    
    def pop2(self):
        if self.top2>(self.sz/2)+1:
            x=self.arr[self.top2]
            self.arr[self.top2]=None
            self.top2-=1
            return x
        else:
            print('Stack2 underflow')

    def peek1(self):
        return self.arr[self.top1]

    def peek2(self):
        return self.arr[self.top2]
            
    def print(self):
        for i, k in enumerate(self.arr):
            print(f' {i}:{k} ',end='')

t=TwoStacks(10)
t.push1(1)
t.push1(2)
t.push1(3)
t.push2(10)
t.push2(20)
t.push2(30)
t.print()

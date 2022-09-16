'''
Two stack efficient method
'''
class TwoStacks:
    def __init__(self,n):
        self.sz=n
        self.arr=[None]*n
        self.top1=-1
        self.top2=self.sz
    
    # Method to push an element in stack1
    def push1(self,x):
        if self.top1<self.top2:
            self.top1+=1
            self.arr[self.top1]=x
        else:
            print('Stack1 overflow')
    # Method to push element in stack2
    def push2(self,x):
        if self.top1<self.top2-1:
            self.top2-=1
            self.arr[self.top2]=x
        else:
            print('Stack2 Overflow')

    def pop1(self):
        if self.top1>-1:
            x=self.arr[self.top1]
            self.arr[self.top1]=None
            self.top1-=1
            return x
        else:
            print('Stack1 Underflow')

    def pop2(self):
        if self.top2<self.sz:
            x=self.arr[self.top2]
            self.arr[self.top2]=None
            self.top2-=1
            return x
        else:
            print('Stack2 Underflow')
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
t.push1(4)
t.push1(5)
t.push2(10)
t.push2(20)
t.push2(30)
t.push2(40)
t.push2(50)
t.pop2()
t.print()

    

# Here we are going to implement stack using Linked List
# We need to pick end,like from where are we going to perform push and pop operation 
# 1.if we push from the end
#   if we take head as the reference all the Operation will require Theta(N) time
#   for insertion and deletion 
#   If we use tail reference deletion will we theta(n) cause we always have to traverse 
#   till second last node and insert will be a constant operation 
# 2.Thats why its always preferred to perform push and pop operation from 
#   the beggining to have T(n)=theta(1)   
# 3. Method implemented in MyStack class
#   push-insert in the stack 
#   pop-remove the last method
#   peek-return the last element in the stack
from math import inf

from numpy import size
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class my_Stack:
    def __init__(self):
        self.head=None
        self.sz=0
    
    def push(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
        self.sz=self.sz+1
    
    def pop(self):
        if self.head==None:
            print("Stack is empty")
            return
        last_element=self.head.data 
        self.head=self.head.next    
        self.sz=self.sz-1
        return last_element
    
    def size(self):
        return self.sz
    
    def peek(self):
        if self.head==None:
            return inf
        return self.head.data

    def print_stack(self):
        curr_ele=self.head
        while curr_ele!=None:
            print(curr_ele.data,end=" ")
            curr_ele=curr_ele.next
        print()

stack=my_Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print('peek',stack.peek())
print('size',stack.size())
print('Stack:',end=" ")
stack.print_stack()
print()
print('pop',stack.pop())
print('pop',stack.pop())
print('pop',stack.pop())
print('pop',stack.pop())
print('pop',stack.pop())
print(stack.peek())
print('Stack:',end=" ")
stack.print_stack()
print()
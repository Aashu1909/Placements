# Queue a user-defined data Structure
# Works First In First Out order.
# enqueue means insertion an element at the rear.
# dequeue means deletion an element from front.
# Time complexity of every ops is o(1)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.siz=0

    def enqueue(self,data):
        temp=Node(data)
        if self.rear==None:
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.siz+=1

    def dequeue(self):
        if self.front==None:
            return None
        res=self.front.data
        self.front=self.front.next
        if self.front==None:
            self.rear=None
        self.siz-=1
        return res

    def getSize(self):
        return self.siz

    def isEmpty(self):
        return False if self.siz!=0 else True

    def getFront(self):
        return self.front.data
    
    def getRear(self):
        return self.rear.data



def print_queue(head):
    curr_ele=head
    while curr_ele!=None:
        print(curr_ele.data,end=" ")
        curr_ele=curr_ele.next
    print()

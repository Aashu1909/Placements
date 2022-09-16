# Doubly Linked List is a user-defined dynamic data Structure
# Each node in the linked list stores the Data and the reference of the next node and previous node
# of the linked list.
# In the last node the next reference will point to null and the prev pointer will 
# point to the element before in the linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class MyDeque:
    def __init__(self) -> None:
        self.front=None
        self.rear=None
        self.sz=0
    
    def size(self):
        return self.sz 
    
    def isEmpty(self):
        return True if self.sz==0 else False
    
    def insertRear(self,element):
        temp=Node(element)
        if self.rear==None:
            self.front=temp
        else:
            self.rear.next=temp
            temp.prev=self.rear
        self.rear=temp
        self.sz+=1

    def insertFront(self,data):
        temp=Node(data)
        if self.front==None:
            self.rear=temp
        else:
            temp.next=self.front
            self.front.prev=temp
        self.front=temp
        self.sz+=1

    def deleteFront(self):
        if self.front==None:
            return None
        res=self.front.data
        self.front=self.front.next
        if self.front==None:
            self.rear=None
        else:
            self.front.prev=None
        self.sz-=1
        return res

    def deleteRear(self):
        if self.rear==None:
            return None
        res=self.rear.data
        self.rear=self.rear.prev
        if self.rear.prev==None:
            self.front=None
        self.rear.next=None
        self.sz-=1
        return res

    def getFront(self):
        return self.front.data if self.front!=None else None

    def getRear(self):
        return self.rear.data if self.rear!=None else None

    def size(self):
        return self.sz

    def print_dequeue(self):
        curr_ele=self.front
        while curr_ele!=None:
            print(curr_ele.data,end=" ")
            curr_ele=curr_ele.next
        print()

d1=MyDeque()
print('insert From front')
d1.insertFront(10)
d1.insertFront(20)
d1.insertFront(30)
d1.insertFront(40)
d1.insertFront(50)
d1.print_dequeue()
print('insert From Rear')
d1.insertRear(20)
d1.insertRear(30)
d1.insertRear(40)
d1.insertRear(50)
d1.print_dequeue()
print("Size",d1.size())
print("Front:",d1.getFront())
print("Rear",d1.getRear())
print(d1.deleteFront())
print(d1.deleteRear())
print(d1.deleteRear())
d1.print_dequeue()
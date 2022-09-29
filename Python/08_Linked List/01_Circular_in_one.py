class Node:
    def __init__(self,x,next=None) -> None:
        self.data=x
        self.next=next
    
def insertAtBeg(head,x):
    temp=Node(x)
    if head==None:
        temp.next=temp
        return temp
    curr=head
    while curr.next!=head:
        curr=curr.next
    curr.next=temp
    temp.next=head
    return temp

def insertAtBegEffi(head,element):
    temp=Node(element)
    if head==None:
        temp.next=temp
        return temp
    temp.next=head.next
    head.next=temp
    temp.data,head.data=head.data,temp.data
    return head

def insertAtEnd(head,x):
    temp=Node(x)
    if head==None:
        temp.next=temp
        return temp
    curr=head
    while curr.next!=head:
        curr=curr.next
    curr.next=temp
    temp.next=head
    return head

def insertAtEndEffi(head,x):
    temp=Node(x)
    if head==None:
        return temp
    temp.next=head.next 
    head.next=temp 
    head.data,temp.data=temp.data,head.data
    return temp
    
def deleteAtBeg(head):
    if head==None or head.next==head:
        return None
    curr=head
    while curr.next!=head:
        curr=curr.next
    temp=head.next
    curr.next=head.next 
    return temp

def deleteAtBegEffi(head):
    if head==None:
        return None
    if head.next==head:
        return None
    head.data=head.next.data
    head.next=head.next.next
    return head

def deleteKth(head,pos):
    if pos==1:
        return deleteAtBeg(head)
    # Because we need to get hold of k-1 node and to get hold of that we need to iterate k-2 times
    curr=head
    for _ in range(pos-2):
        curr=curr.next
    curr.next=curr.next.next 
    return head

def printCLL(head):
    if head==None:
        return None
    print(head.data,end=" ")
    curr=head.next
    while curr!=head:
        print(curr.data,end=" ")
        curr=curr.next 
    print()

temp=[10,20,30,40,50,60]
# head=insertAtBeg()
head=None
for i in temp:
    head=insertAtEnd(head,i)
    print(head.data,i)
printCLL(head)
head=deleteAtBeg(head)
printCLL(head)

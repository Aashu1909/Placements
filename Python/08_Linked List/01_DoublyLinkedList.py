class Node:
    def __init__(self,data,next=None,prev=None) -> None:
        self.data=data
        self.prev=next
        self.next=prev
    
def insertAtBeg(head,x):
    temp=Node(x)
    if head==None:
        return temp
    temp.next=head
    head.prev=temp
    return temp

def insertAtEnd(head,x):
    temp=Node(x)
    if head==None:
        return temp
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=temp
    temp.prev= curr
    return head

def deleteAtBeg(head):
    if head==None:
        return None
    if head.next==None:
        return None
    head=head.next
    head.prev=None
    return head

def deleteAtEnd(head):
    if head==None:
        return None
    if head.next==None:
        return None
        
    curr=head
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head

def reverse(head):
    if head==None:
        return None
    if head.next==None:
        return head
    curr=head
    prev=None
    while curr!=None:
        prev=curr
        curr.prev,curr.next=curr.next,curr.prev
        curr=curr.prev
    return prev

def print_dll(head):
    if head==None:
        return None
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next 
    print()

temp=[10,20,30,40,55,60,65,15,89]
head=None
for i in temp:
    head=insertAtBeg(head,i)
print_dll(head)
head=reverse(head)
print_dll(head)
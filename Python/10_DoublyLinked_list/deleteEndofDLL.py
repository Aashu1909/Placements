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

def deleteEndofDLL(head):
    if head==None:
        return None
    if head.next==None:
        return None
    curr=head
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head


def insertAtEnd(head,data):
    temp=Node(data)
    if head==None:
        return temp
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=temp
    temp.prev=curr
    return head

def print_doublylinked_list(head):
    curr_ele=head
    while curr_ele!=None:
        print(curr_ele.data,end=" ")
        curr_ele=curr_ele.next
    print()
head=None
head=insertAtEnd(head,10)
head=insertAtEnd(head,20)
head=insertAtEnd(head,30)
head=insertAtEnd(head,40)
head=insertAtEnd(head,50)
print_doublylinked_list(head)
head=deleteEndofDLL(head)
head=deleteEndofDLL(head)
head=deleteEndofDLL(head)
head=deleteEndofDLL(head)
head=deleteEndofDLL(head)
print(print_doublylinked_list(head))

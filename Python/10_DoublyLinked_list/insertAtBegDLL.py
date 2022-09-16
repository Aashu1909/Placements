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

def insertAtBeg(head,data):
    temp=Node(data)
    if head==None:
        return temp
    head.prev=temp
    temp.next=head
    return temp #new head  

def print_doublylinked_list(head):
    curr_ele=head
    while curr_ele!=None:
        print(curr_ele.data,end=" ")
        curr_ele=curr_ele.next
    print()

def print_reverse_DoublyLinkedList(head):
    curr=head
    while curr.next!=None:
        curr=curr.next
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.prev
    print()

head=None
head=insertAtBeg(head,10)
# head=insertAtBeg(head,20)
# head=insertAtBeg(head,30)
# head=insertAtBeg(head,40)
# head=insertAtBeg(head,50)
print_doublylinked_list(head)
print_reverse_DoublyLinkedList(head)
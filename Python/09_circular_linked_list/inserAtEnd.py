# Linked List is a user-defined dynamic data Structure
# Each node in the linked list stores the Data and the reference of the next node of the linked list.
# In the last node the reference will point to null in the linked list

# Insert at end of the circular linked list
# O(n) o(1)space
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insertAtEnd(head,element):
    temp=node(element)
    if head==None:
        temp.next=temp
        return temp
    curr=head
    while curr.next!=head:
        curr=curr.next
    curr.next=temp
    temp.next=head
    return head

def print_circular_linked_list(head):
    if head==None:
        return None
    print(head.data,end=" ")
    curr=head.next
    while curr!=head:
        print(curr.data,end=" ")
        curr=curr.next
head=None
head=insertAtEnd(head,10)
head=insertAtEnd(head,20)
head=insertAtEnd(head,30)
head=insertAtEnd(head,50)
head=insertAtEnd(head,40)
print_circular_linked_list(head)
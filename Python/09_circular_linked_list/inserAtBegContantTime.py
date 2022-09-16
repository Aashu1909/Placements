# Linked List is a user-defined dynamic data Structure
# Each node in the linked list stores the Data and the reference of the next node of the linked list.
# In the last node the reference will point to null in the linked list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Here the idea is to first create the node and
# set the next element of the created node to head's next and swap the value of head and node created
def insertAtBeg(head,element):
    temp=node(element)
    if head==None:
        temp.next=temp
        return temp
    temp.next=head.next
    head.next=temp
    temp.data,head.data=head.data,temp.data
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
head=insertAtBeg(head,10)
head=insertAtBeg(head,20)
head=insertAtBeg(head,30)
head=insertAtBeg(head,40)
head=insertAtBeg(head,50)
head=insertAtBeg(head,60)
print_circular_linked_list(head)
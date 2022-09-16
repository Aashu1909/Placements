# Linked List is a user-defined dynamic data Structure
# Each node in the linked list stores the Data and the reference of the next node of the linked list.
# In the last node the reference will point to null in the linked list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_at_end(head,data):
    if head is None:
        return node(data)
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=node(data)
    return head

def print_linked_list(head):
    curr_ele=head
    while curr_ele!=None:
        print(curr_ele.data,end=" ")
        curr_ele=curr_ele.next
    print()

head=None
head=insert_at_end(head,10)
head=insert_at_end(head,20)
head=insert_at_end(head,30)
head=insert_at_end(head,40)
head=insert_at_end(head,50)
head=insert_at_end(head,60)
print_linked_list(head)
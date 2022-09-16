# Linked List is a user-defined dynamic data Structure
# Each node in the linked list stores the Data and the reference of the next node of the linked list.
# In the last node the reference will point to null in the linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse_list(head):
    # We here have to explicitly handel cases where 
    # Head==None head.next==None
    if head==None:
        return None
    if head.next==None:
        return head
    rest_head=reverse_list(head.next)
    rest_tail=head.next
    rest_tail.next=head
    head.next=None
    return rest_head

def print_linked_list(head):
    curr_ele=head
    while curr_ele!=None:
        print(curr_ele.data,end=" ")
        curr_ele=curr_ele.next
    print()

head=None
head = node(10)
head.next = node(20)
head.next.next = node(30)
head.next.next.next = node(40)
head.next.next.next.next = node(50)
print_linked_list(head)
head = reverse_list(head)
print_linked_list(head)
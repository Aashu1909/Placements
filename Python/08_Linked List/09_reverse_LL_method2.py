# Linked List is a user-defined dynamic data Structure
# Each node in the linked list stores the Data and the reference of the next node of the linked list.
# In the last node the reference will point to null in the linked list


# Here we are first reversing the list and then making the call for next
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse_Linked(curr,prev=None):
    if curr==None:
        return prev
    next=curr.next
    curr.next=prev
    return reverse_Linked(curr=next,prev=curr)

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
head = reverse_Linked(head)
print_linked_list(head)
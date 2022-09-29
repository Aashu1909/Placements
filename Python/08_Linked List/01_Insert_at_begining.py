# Linked List is a user-defined dynamic data Structure
# Each node in the linked list stores the Data and the reference of the next node of the linked list.
# In the last node the reference will point to null in the linked list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert_at_begining(head,data):
    temp=node(data)
    temp.next=head
    # return head of the modified linked list
    return temp

def print_linked_list(head):
    curr_ele=head
    while curr_ele!=None:
        print(curr_ele.data,end=" ")
        curr_ele=curr_ele.next
    print()
    

def recursive_print(head):
    if head==None:
        return 
    recursive_print(head.next)
    print(head.data,end=" ")

head=None
head=insert_at_begining(head,10)
head=insert_at_begining(head,20)
head=insert_at_begining(head,30)
head=insert_at_begining(head,40)
head=insert_at_begining(head,50)
print_linked_list(head)
recursive_print(head)
# Linked List is a user defined dynamic data Structure
# Each node in the linked list stores the Data and the reference of the next node of the linked list.
# In the last node the reference will point to null in the linked list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None


def print_linked_list(head):
    curr_ele=head
    while (curr_ele!=None):
        print(curr_ele.data,end=" ")
        curr_ele=curr_ele.next
    print()

temp=node(10)
head=temp
temp1=node(30)
temp2=node(20)
temp3=node(40)
temp.next=temp1
temp1.next=temp2
temp2.next=temp3
print_linked_list(head)
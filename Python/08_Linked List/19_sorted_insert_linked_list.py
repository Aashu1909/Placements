# Linked List is a user-defined dynamic data Structure
# Each node in the linked list stores the Data and the reference of the next node of the linked list.
# In the last node the reference will point to null in the linked list
# O(N) and O(1)
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def sorted_insert(head,data):
    # If head is empty
    if head==None:
        temp=node(data)
        return temp
    # if the Ll contains only one node
    if (head.data>data):
        temp=node(data)
        temp.next=head
        return temp
    # Here we find the prev of the node with is greater than Data to be inserted
    curr=head
    while(curr.next!=None) and (curr.next.data<data):
        curr=curr.next
    temp=node(data)
    temp.next=curr.next
    curr.next=temp
    return head

def print_linked_list(head):
    if head==None:
        return None

    curr_ele=head
    while curr_ele!=None:
        print(curr_ele.data,end=" ")
        curr_ele=curr_ele.next
    print()

head=None
# head = node(10)
# head.next = node(20)
# head.next.next = node(30)
# head.next.next.next = node(40)
# head.next.next.next.next = node(50)
print_linked_list(head)
head = sorted_insert(head,60)
print_linked_list(head)
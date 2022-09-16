# Linked List is a user-defined dynamic data Structure
# Each node in the linked list stores the Data and the reference of the next node of the linked list.
# In the last node the reference will point to null in the linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Here we have used the stack for reversing we forst stores all the element in the stack 
# Then pop the element out the rewrite the data in the node of LL.
def reverse_a_linked_list(head):
    stack=[]
    curr=head
    while curr!=None:
        stack.append(curr.data)
        curr=curr.next
    curr=head
    while curr!=None:
        curr.data=stack.pop()
        curr=curr.next
    return head


# here the idea is to reverse the links of the linked list to obtain the required result
# This type of arrangement requires O(1) aux space and O(n) time complexity
def efficientReverse(head):
    prev=None
    curr=head
    while curr!=None:
        nextt=curr.next
        curr.next=prev
        prev=curr
        curr=nextt
    return prev
        

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
head = reverse_a_linked_list(head)
print_linked_list(head)
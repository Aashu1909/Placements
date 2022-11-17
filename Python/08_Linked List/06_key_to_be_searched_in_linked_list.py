# Linked List is a user-defined dynamic data Structure
# Each node in the linked list stores the Data and the reference of the next node of the linked list.
# In the last node the reference will point to null in the linked list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

# This function will return the position of the element of the linked list
def search_in_linked_list(head,x):
    pos=1
    curr_ele=head
    while (curr_ele!=None):
        if (curr_ele.data==x):
            return pos
        pos+=1
        curr_ele=curr_ele.next
    return -1

def recursive_search(head,x):
    if head==None:
        return -1 
    if head.data==x:
        return 1
    res=recursive_search(head.next,x)
    if res==-1:
        return -1
    return res
    
head=node(10)
head.next=node(15)
head.next.next=node(20)
head.next.next.next=node(25)
head.next.next.next.next=node(30)
print(search_in_linked_list(head,25))
print(recursive_search(head,25))
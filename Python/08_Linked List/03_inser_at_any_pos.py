# Linked List is a user-defined dynamic data Structure
# Each node in the linked list stores the Data and the reference of the next node of the linked list.
# In the last node the reference will point to null in the linked list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def insert_at_given_pos(head,data,pos):
    temp=node(data)
    if pos==1:
        temp.next=head
        # return head
        return  temp
    curr=head
    for _ in range(pos-1):
        curr=curr.next
    # Corner case when position is greater than num_of_nodes
    if curr==None: return None
    
    temp_next=curr.next
    curr.next=temp
    temp.next=temp_next
    return head

def print_linked_list(head):
    curr_ele=head
    while curr_ele!=None:
        print(curr_ele.data,end=" ")
        curr_ele=curr_ele.next
    print()

head = node(10)
head.next = node(20)
head.next.next = node(30)
head.next.next.next = node(40)
head.next.next.next.next = node(50)
print_linked_list(head)
head = insert_at_given_pos(head,45,4)
print_linked_list(head)
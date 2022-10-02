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
    
def pairwiseSwap(head):
    #code here
    if head==None and head.next==None:
        return head
    prev=head
    curr=head.next.next
    head=head.next
    head.next=prev
    while curr and curr.next:
        # print(prev.data,curr.data)
        prev.next=curr.next
        prev=curr
        nxt=curr.next.next
        (curr.next).next=prev
        curr=nxt
    # Odd Nodes 
    if curr!=None:
        prev.next=curr
    else:
        prev.next=None
    return head
    
temp=[1 ,2 ,3, 4 ,5 ,6]
head=None 
for i in temp[::-1]:
    head=insert_at_begining(head,i)
print_linked_list(head)
head=pairwiseSwap(head)
print_linked_list(head)
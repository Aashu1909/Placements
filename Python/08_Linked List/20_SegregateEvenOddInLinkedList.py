class node:
    def __init__(self,data):
        self.data=data
        self.next=None

# The idea is to keep connecting even nodes togother to form a even linked
# list by changing the links and keep track of even end 
# We do similar thing with the odd nodes and at the last we connect the EvenEnd with OddStart

def segregateEvenOdd(head):
    evenStart=None;evenEnd=None;oddStart=None;oddEnd=None
    curr=head
    while curr!=None:
        if curr.data%2==0:
            if evenStart==None:
                evenStart=curr
                evenEnd=evenStart
            else:
                evenEnd.next=curr
                evenEnd=evenEnd.next
        else:
            if oddStart==None:
                oddStart=curr
                oddEnd=oddStart
            else:
                oddEnd.next=curr
                oddEnd=oddEnd.next
        curr=curr.next
    
    # This statment is to capture the Edge case which is All nodes Even Or Odd
    if oddStart==None or evenStart==None:
        return head
    evenEnd.next=oddStart
    oddEnd.next=None
    return evenStart

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
    
head=None
head=insert_at_begining(head,1)
head=insert_at_begining(head,2)
head=insert_at_begining(head,3)
head=insert_at_begining(head,4)
head=insert_at_begining(head,5)
head=insert_at_begining(head,6)
head=insert_at_begining(head,7)
head=insert_at_begining(head,9)
print_linked_list(head)
newHead=segregateEvenOdd(head)
print_linked_list(newHead)

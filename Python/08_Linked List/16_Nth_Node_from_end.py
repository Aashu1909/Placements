# Method 1
def NthNodefromEnd(head,n):
    curr=head
    count=0
    while curr!=None:
        count+=1
        curr=curr.next
    curr=head
    for _ in range(count-n+1):
        curr=curr.next
    return curr.data
    

# Method 2 Two Pointer
# Here the idea is to intitalize first and second pointer
# We move the first pointer n position ahead of the second,after that move both the pointer by
# one till the first pointer becomes NULL
def nthFromEnd(head,n):
    if head==None:
        return None
    first,second=head,head
    for _ in range(n):
        # if linked list is less than n
        if first==None:
            return None
        first=first.next

    while first!=None:
        second=second.next 
        first=first.next

    return second.data
    
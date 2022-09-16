# Remove element from sorted linked list 
def removeDuplicates(head):
    curr=head
    while curr!=None and curr.next!=None:
        if curr.data==curr.next.data:
            curr=curr.next.next
        else:
            curr=curr.next
    return head


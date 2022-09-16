# Method 1 Swapping data from adjacent nodes
# We increase the pointer by 2 places each time and swap the data 
def pairWiseSwap(head):
    curr=head
    while curr!=None and curr.next!=None:
        curr.data,curr.next.data=curr.next.data,curr.data
        curr=curr.next.next
    return head


def pairWiseSwap2(head):
    if head==None:
        return None
      # We have explicitly Handled start of linked Otherwise we have to put IF statement in the while loop
    prev=head
    curr=head.next.next
    head=head.next
    head.next=prev
    """
    so Lets Assume a linked list 
    1->2->3->4->5->6
    First changing its head
    2->1 3->4->5->6
    prev=1 curr=3
    prev.next=curr.next
    2->1->4 and 3->4->5->6
    4 is the same node which is pointed by two Pointer 
    prev=curr->3
    nextt=curr.next.next->5
    3=curr
    3.next->4.next=curr->3
    curr=nextt->5
    """
    # We have explicitly Handled start of linked Otherwise we have to put IF statement in the while loop
    while curr!=None and curr.next!=None:
        prev.next=curr.next
        prev=curr
        nextt=curr.next.next
        curr.next.next=curr
        curr=nextt
    prev.next=curr

    return head
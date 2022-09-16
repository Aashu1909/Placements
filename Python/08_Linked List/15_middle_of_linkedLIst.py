
def middleLinkedList(head):
    if head==None:
        return None
    slow,fast=head,head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
    return slow.data

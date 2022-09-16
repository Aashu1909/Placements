# The idea is to initialize Slow and fast Pointer
# if they meet each other that means there exit a loop in the given linked list
# Otherwise no loop detected
# We have to move slow pointer by one and fast pointer by 2
def isloop(head):
    slow,fast=head,head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False
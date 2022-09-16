# Using Floyd Cycle Detection 
# its an extension to the previos problem of Loop detection
# So the approch is to first find where the slow and fast became equal 
# after that break the loop and make slow pointer start from head and increase them by one each till 
# Next of slow is not equal to next of fast 

def detectRemoveLoop(head):
    slow=fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    # Checking if fast pointer is null of not,Means the i/p doesnt contain a loop
    if slow!=fast:
        return False
    # then making slow start from head and moving both pointer one by one till they are same
    slow=head
    while slow.next!=fast.next:
        slow=slow.next
        fast=fast.next
    # Then making the next of the fast pointer NONE
    fast.next=None

    
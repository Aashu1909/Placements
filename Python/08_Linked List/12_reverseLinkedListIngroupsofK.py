# Recursive solution
def reverseLinkedList(head,k):
    curr=head
    nextt=None
    prev=None
    count=0
    while curr!=None and count<k:
        nextt=curr.next
        curr.next=prev
        prev=curr
        curr=nextt
        count+=1

    if nextt!=None:
        restHead=reverseLinkedList(nextt,k)
        head.next=restHead
    return prev

# Variation of the above question
#if the nodes left is less than k& dont reverse it
def isValid(head,k):
    curr=head
    while curr!=None and k>0:
        curr=curr.next
        k-=1
    return (k==0)

def reverseLinkedList(head,k):
    curr=head
    nextt=None
    prev=None
    count=0
    while curr!=None and count<k:
        nextt=curr.next
        curr.next=prev
        prev=curr
        curr=nextt
        count+=1
    if nextt!=None:
        if isValid(nextt,k):
            restHead=reverseLinkedList(nextt,k)
            head.next=restHead
        else:
            head.next=nextt    
    return prev




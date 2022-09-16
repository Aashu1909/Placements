# Iterative Version of reverse linked list in group of k
def reverseKNode(head,k):
    curr=head
    prevFirst=head
    isFirstPass=True
    while curr!=None:
        first=curr
        prev=None
        count=0
        while curr!=None and count<k:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
            count+=1
        if isFirstPass:
            head=prev
            isFirstPass=False
        else:
            prevFirst.next=prev
        
        prevFirst=first
    
    return head
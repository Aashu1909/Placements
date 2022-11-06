# to merge two sorted linked list
def MergeLinkedList(a,b):
    if a==None:
        return b
    if b==None:
        return a
    head=None
    tail=None
    if a.val<=b.val:
        head=tail=a
        a=a.next
    else:
        head=tail=b
        b=b.next
    
    while a!=None and b!=None:
        if (a.val<=b.val):
            tail.next=a
            tail=a
            a=a.next
        else:
            tail.next=b
            tail=b
            b=b.next
    if a==None:
        tail.next=b
    else:
        tail.next=a
    return head
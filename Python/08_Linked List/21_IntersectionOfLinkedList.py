# METHOD 1
# Create a emplty hashset 
# traverse the first linkedlist and put all the element in hashset.
# Traverse second linked list as soon as we find the address of linked in hashset return the ans

def findIntersection(head1,head2):
    hashset=set()
    curr=head1
    while curr!=None:
        hashset.add(curr)
        curr=curr.next
    
    curr=head2
    while curr!=None:
        if curr in hashset:
            return curr.data
        curr=curr.next
    return None


# METHOD2
# this method requires 4 iterations and first two to count no of nodes in Ll
# Then travese the beeger by abs(l1-l2) time 
# then traversing both together

def findIntersection2(head1,head2):
    curr=head1
    # Count of List 1
    count1=0
    while curr!=None:
        count1+=1
        curr=curr.next 
    # Count of list 2
    count2=0
    curr=head2
    while curr!=None:
        count2+=1
        curr=curr.next
    # Finding the abs diff and assigning the head to the bigger linked list
    if count1>count2:
        diff=abs(count1-count2)
        curr1=head1
    else:
        diff=abs(count2-count1)
        curr1=head2
    
    curr2=head1 if curr1!=head1 else head2
    
    count=0
    while curr1!=None and count<diff:
        count+=1
        curr1=curr1.next

    while curr1!=None and curr2!=None:
        if curr1==curr2:
            return curr.data
        curr1=curr1.next
        curr2=curr2.next    
    
    return None
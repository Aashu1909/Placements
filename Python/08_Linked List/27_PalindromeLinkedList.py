# a naive solution is to use a stack and keep pushing the value in it
# Then in sescond traversal we keep poping and matching the value in the linkedlist 
# if we find a mismatch we return false


# Method 2 Efiicient 
"""The solution here is to first find the middle and then reverse the linked list after the middle node
Then checking there value one by one if mismatch is found then return False
if we reach the end of the list then return True
"""

def reverseList(head):
    if head==None:
        return None
    prev=None
    curr=head
    while curr!=None:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    return prev

def palindromeLinkedList(head):
    slow=fast=head
    while fast.next!=None and fast.next.next!=None:
        slow=slow.next
        fast=fast.next.next
    
    rev=reverseList(slow.next)
    curr=head
    while rev!=None:
        if rev.val!=curr.val:
            return False
        rev=rev.next
        curr=curr.next
    return True
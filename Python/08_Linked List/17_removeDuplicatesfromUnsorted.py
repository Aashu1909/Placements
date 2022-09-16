def removeDuplicatesFromunsorted(head):
        # Base case of empty list or
        # list with only one element
        if head is None or head.next is None:
            return head
        # Hash to store seen values
        hash = set()
        current = head
        hash.add(head.data)
        while current.next!=None:
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
 
        return head
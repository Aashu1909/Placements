    def findMid(self,head):
        slow, fast=head, head.next
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
                
    def merge(self,head1,head2):
        if head1==None: return head2
        if head2==None: return head1
        
        head=tail=None
        if head1.data>head2.data:
            tail=head=head2
            head2=head2.next
        else:
            head=tail=head1
            head1=head1.next
        
        while head1!=None and head2!=None:
            if head1.data>head2.data:
                tail.next=head2
                head2=head2.next
                tail=tail.next
            else:
                tail.next=head1
                head1=head1.next
                tail=tail.next
        
        if head1==None:
            tail.next=head2
        if head2==None:
            tail.next=head1
        return head    
        
    
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        left=head
        right=self.findMid(head)
        tmp=right.next
        right.next=None
        right=tmp
        left=self.mergeSort(left)
        right=self.mergeSort(right)
        return self.merge(left,right)
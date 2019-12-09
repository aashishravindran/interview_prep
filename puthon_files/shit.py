

 dummy=ListNode(0)
        dummy.next=head        
        
        l=1
        curr=head
        
        while curr.next is not None:
            l+=1
            curr=curr.next
        
        curr=dummy ## making current point to the first node again 
        l-=n
        while l>0:
            l-=1
            curr=curr.next
        curr.next=curr.next.next
        return dummy.next
        
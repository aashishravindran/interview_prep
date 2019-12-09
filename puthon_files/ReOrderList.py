# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 143. Reorder List
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        def reverse(l2):
            prev=None
            curr=l2
            while curr is not None:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        
        def merge(l1,l2):
            print("here")
            while l1 is not None:
                l1_next=l1.next
                l2_next=l2.next 
                
                l1.next=l2
                
                if l1_next is None:
                    break
                    
                l2.next=l1_next
                l1=l1_next
                l2=l2_next
        
        
        if not head or not head.next:
            return 
        h=head
        slow=head 
        fast=head
        prev=None
        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        
       
        prev.next=None
        
        l2=reverse(slow)
        merge(h,l2)
        
        
        
        
        
        
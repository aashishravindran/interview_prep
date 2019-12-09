# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergetwoList(l1,l2):
            
            dummy=ListNode(None)
            dummy_wp=dummy
            l1_wp=l1
            l2_wp=l2
            while l1_wp and l2_wp:
                if l1_wp.val<=l2_wp.val:
                    
                    dummy_wp.next=l1_wp
                    if l1_wp is not None:
                        l1_wp=l1_wp.next
                else:
                    dummy_wp.next=l2_wp
                    if l2_wp is not None:
                        l2_wp=l2_wp.next
        
                dummy_wp=dummy_wp.next
        
            dummy_wp.next= l1_wp if l1_wp is not None else l2_wp
            return dummy.next
        
        
        
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        
        mid=len(lists)//2
        left=self.mergeKLists(lists[:mid])
        
        right=self.mergeKLists(lists[mid:])
        return mergetwoList(left,right)

        
    
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
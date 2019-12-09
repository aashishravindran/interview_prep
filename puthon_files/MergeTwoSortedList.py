# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(None)
        dummy_wp=dummy
        l1_wp=l1
        l2_wp=l2
        while l1_wp and l2_wp:
            if l1_wp.val<l2_wp.val:
                print("jere")
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
        
        
        
        
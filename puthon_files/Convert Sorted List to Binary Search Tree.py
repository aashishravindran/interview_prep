# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# time complexity O(NlogN) since we are traversing the linked list each time to find the middle 
# space complexity o(logn)
class Solution(object):
    def findmiddle(self,head):
            prev=None
            slow=head 
            fast=head 
            while fast is not None and fast.next is not None:
                
                prev=slow
                slow=slow.next
                fast=fast.next.next
                
            if prev:
                    prev.next=None
                
            return slow 
            
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
             
        mid = self.findmiddle(head)
        root=TreeNode(mid.val)
        if head == mid:
               return root
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(mid.next)
        return root
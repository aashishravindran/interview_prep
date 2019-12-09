https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums,left,right):
            if left==right:
                return 
            mid=left+((right-left)/2)
            root=TreeNode(nums[mid])
            root.left=helper(nums,left,mid)
            
            root.right=helper(nums,mid+1,right)
            
            return root
        
        return helper(nums,0,len(nums))

'''
convert head to array and iterare 
'''
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

class Solution(object):
    def __init__(self):
        self.res=[]
    def convertToArr(self,head):
        
        curr=head
        while curr:
            self.res.append(curr.val)
            curr=curr.next
        return 
         
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.convertToArr(head)
        print(self.res)
        def helper(left,right):
            if left==right:
                return 
            mid =left+((right-left)/2)
            midval=self.res[mid]
            #print(midval)
            root=TreeNode(midval)
            
            root.left=helper(left,mid)
            root.right=helper(mid+1,right)
            
            return root
        
        return helper(0,len(self.res))
            
        
        
        	
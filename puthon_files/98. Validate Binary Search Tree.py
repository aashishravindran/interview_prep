# https://leetcode.com/problems/validate-binary-search-tree/submissions/
#98. Validate Binary Search Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# Intutive non Optimal solution would be to generate an rray from the Tree using in order tarversal and chek if that array is sorted
##  


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_val_helper(root,low,high):
            if not root:
                return True
            if root.val <=low or root.val>=high:
                return False
            
            if not is_val_helper(root.left,low,root.val):
                return False
            
            if not is_val_helper(root.right,root.val,high):
                return False
            return True
        return is_val_helper(root,float('-inf'),float('inf'))
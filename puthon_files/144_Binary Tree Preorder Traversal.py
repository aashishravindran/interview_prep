# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/binary-tree-preorder-traversal/

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def preOrderHelper(root):
            if root is None:
                return 
            res.append(root.val)
            preOrderHelper(root.left)
            preOrderHelper(root.right)
            
            
        preOrderHelper(root)
        return res